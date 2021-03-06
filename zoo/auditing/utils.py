import hashlib


def create_git_issue(issue, user_name, reverse_url):
    remote_iid = issue.repository.scm_module.create_remote_issue(
        issue, user_name, reverse_url
    )
    issue.remote_issue_id = remote_iid
    issue.full_clean()
    issue.save()


def get_md5_hash(string):
    return hashlib.md5(string).hexdigest()
