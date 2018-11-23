from collections import namedtuple

import arrow
import structlog

from .models import Issue

log = structlog.get_logger()

Result = namedtuple("Result", ["issue_key", "is_found", "details"])
# set default to `None` for `details`
Result.__new__.__defaults__ = (None,)


class CheckContext:
    Result = Result

    def __init__(self, repository, repo_path):
        self.owner = repository.owner
        self.name = repository.name
        self.repo_url = repository.url
        self.remote_id = repository.remote_id
        self.provider = repository.provider
        self.path = repo_path
        self.languages = repository.languages_from_analytics


def determine_issue_status(is_found, old_status):
    if is_found:
        if old_status == Issue.Status.NOT_FOUND.value:
            return Issue.Status.NEW.value

        if old_status == Issue.Status.FIXED.value:
            return Issue.Status.REOPENED.value

    else:
        if old_status != Issue.Status.NOT_FOUND.value:
            return Issue.Status.FIXED.value

    return old_status


def save_check_result(issue_repo, issue_key, is_found, details=None):
    if details is None:
        details = {}

    # we ignore/clear details for not found (or fixed) issues
    if not is_found:
        details = {}

    try:
        issue = issue_repo.issues.get(kind_key=issue_key)
    except Issue.DoesNotExist:
        status = Issue.Status.NEW.value if is_found else Issue.Status.NOT_FOUND.value
        Issue.objects.create(
            repository=issue_repo, kind_key=issue_key, status=status, details=details
        )
    else:
        if issue.details != details:
            issue.details = details
        issue.status = determine_issue_status(is_found, issue.status)
        issue.last_check = arrow.utcnow().datetime
        issue.save()


def check_repository(checks, repository, repo_path):
    context = CheckContext(repository, repo_path)
    for check in checks:
        try:
            for result in check(context):
                # skip unknown results
                if result.is_found is None:
                    continue

                if result.is_found:
                    log.info(
                        "auditing.check.result_found",
                        repo_id=repository.id,
                        check=check.__name__,
                        check_module=check.__module__,
                        issue=result.issue_key,
                    )

                yield result
        except:
            log.exception(
                "auditing.check.error",
                repo_id=repository.id,
                check=check.__name__,
                check_module=check.__module__,
            )


def run_checks_and_save_results(checks, repository, repo_path):
    for result in check_repository(checks, repository, repo_path):
        save_check_result(repository, result.issue_key, result.is_found, result.details)