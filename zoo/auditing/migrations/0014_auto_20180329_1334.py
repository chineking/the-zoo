# Generated by Django 2.0.3 on 2018-03-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("auditing", "0013_auto_20180329_1249")]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="kind_key",
            field=models.CharField(
                choices=[
                    (
                        "gitlab_config:require_approvals",
                        "gitlab_config:require_approvals",
                    ),
                    ("gitlab_config:use_rebase", "gitlab_config:use_rebase"),
                    (
                        "gitlab_config:reset_approvals_on_push",
                        "gitlab_config:reset_approvals_on_push",
                    ),
                    (
                        "gitlab_config:block_on_discussions",
                        "gitlab_config:block_on_discussions",
                    ),
                    (
                        "gitlab_config:block_on_ci_failure",
                        "gitlab_config:block_on_ci_failure",
                    ),
                    ("gitlab_config:autocancel_ci", "gitlab_config:autocancel_ci"),
                    ("gitlab_config:protect_master", "gitlab_config:protect_master"),
                    (
                        "py_requirements:use_pip_compile",
                        "py_requirements:use_pip_compile",
                    ),
                    ("py_requirements:use_netrc", "py_requirements:use_netrc"),
                    (
                        "py_requirements:set_extra_index_url",
                        "py_requirements:set_extra_index_url",
                    ),
                    (
                        "py_requirements:replace_pycrypto",
                        "py_requirements:replace_pycrypto",
                    ),
                    ("py_requirements:replace_ujson", "py_requirements:replace_ujson"),
                    (
                        "py_requirements:use_global_tox",
                        "py_requirements:use_global_tox",
                    ),
                    (
                        "py_requirements:use_global_pip_tools",
                        "py_requirements:use_global_pip_tools",
                    ),
                    (
                        "py_requirements:remove_py2_only_reqs",
                        "py_requirements:remove_py2_only_reqs",
                    ),
                    (
                        "py_requirements:keep_https_enforced",
                        "py_requirements:keep_https_enforced",
                    ),
                    ("readme:have_readme_file", "readme:have_readme_file"),
                    ("readme:add_documentation_info", "readme:add_documentation_info"),
                    ("readme:add_channel_link", "readme:add_channel_link"),
                    ("readme:add_repo_maintainers", "readme:add_repo_maintainers"),
                    ("readme:add_usage_header", "readme:add_usage_header"),
                    (
                        "readme:add_contributing_header",
                        "readme:add_contributing_header",
                    ),
                    (
                        "readme:remove_private_channels",
                        "readme:remove_private_channels",
                    ),
                    ("readme:outdated_file", "readme:outdated_file"),
                    ("dockerfile:ssh_used", "dockerfile:ssh_used"),
                    ("dockerfile:use_yarn", "dockerfile:use_yarn"),
                    ("dockerfile:use_apk_virtual", "dockerfile:use_apk_virtual"),
                    ("dockerfile:use_no_cache", "dockerfile:use_no_cache"),
                    ("dockerfile:remove_maintainer", "dockerfile:remove_maintainer"),
                    ("dockerfile:use_copy", "dockerfile:use_copy"),
                    ("dockerfile:add_cmd", "dockerfile:add_cmd"),
                    (
                        "dockerfile:change_default_user",
                        "dockerfile:change_default_user",
                    ),
                    (
                        "dockerfile:merge_run_instructions",
                        "dockerfile:merge_run_instructions",
                    ),
                    ("dockerfile:multiple_expose", "dockerfile:multiple_expose"),
                    ("dockerfile:privileged_port", "dockerfile:privileged_port"),
                    ("dockerfile:pin_image_version", "dockerfile:pin_image_version"),
                    ("dockerfile:use_alpine_image", "dockerfile:use_alpine_image"),
                    (
                        "dockerfile:use_latest_alpine_image",
                        "dockerfile:use_latest_alpine_image",
                    ),
                    ("dockerfile:change_workdir", "dockerfile:change_workdir"),
                    ("dockerfile:use_workdir", "dockerfile:use_workdir"),
                    ("dockerfile:delete_netrc", "dockerfile:delete_netrc"),
                    (
                        "dockerfile:use_pip_custom_platform",
                        "dockerfile:use_pip_custom_platform",
                    ),
                    (
                        "dockerfile:pip_custom_platform_mismatch",
                        "dockerfile:pip_custom_platform_mismatch",
                    ),
                    (
                        "gitlab_ci:use_docker_cache_from",
                        "gitlab_ci:use_docker_cache_from",
                    ),
                    (
                        "gitlab_ci:ci_build_ref_slug_defined",
                        "gitlab_ci:ci_build_ref_slug_defined",
                    ),
                    (
                        "gitlab_ci:deprecated_variables_used",
                        "gitlab_ci:deprecated_variables_used",
                    ),
                    (
                        "gitlab_ci:hardcoded_registry_url",
                        "gitlab_ci:hardcoded_registry_url",
                    ),
                    (
                        "gitlab_ci:hardcoded_registry_username",
                        "gitlab_ci:hardcoded_registry_username",
                    ),
                    ("gitlab_ci:docker_outdated", "gitlab_ci:docker_outdated"),
                    ("gitlab_ci:coala_outdated", "gitlab_ci:coala_outdated"),
                    ("gitlab_ci:pin_build_images", "gitlab_ci:pin_build_images"),
                    (
                        "dockerignore:create_dockerignore",
                        "dockerignore:create_dockerignore",
                    ),
                    ("dockerignore:ignore_dotgit", "dockerignore:ignore_dotgit"),
                    (
                        "setup_py:use_dependency_gathering_snippet",
                        "setup_py:use_dependency_gathering_snippet",
                    ),
                    ("setup_py:missing_author", "setup_py:missing_author"),
                    ("setup_py:wrong_author_email", "setup_py:wrong_author_email"),
                    (
                        "setup_py:wrong_private_settings",
                        "setup_py:wrong_private_settings",
                    ),
                    ("coafile:create_coafile", "coafile:create_coafile"),
                    (
                        "coafile:dont_use_default_section",
                        "coafile:dont_use_default_section",
                    ),
                    ("coafile:set_inheritance", "coafile:set_inheritance"),
                    ("coafile:use_LineCountBear", "coafile:use_LineCountBear"),
                    ("coafile:use_GitCommitBear", "coafile:use_GitCommitBear"),
                    (
                        "coafile:use_SpaceConsistencyBear",
                        "coafile:use_SpaceConsistencyBear",
                    ),
                    (
                        "coafile:use_DockerfileLintBear",
                        "coafile:use_DockerfileLintBear",
                    ),
                    ("coafile:use_MarkdownBear", "coafile:use_MarkdownBear"),
                    ("coafile:use_YAMLLintBear", "coafile:use_YAMLLintBear"),
                    ("coafile:use_PEP8Bear", "coafile:use_PEP8Bear"),
                    ("coafile:use_PyDocStyleBear", "coafile:use_PyDocStyleBear"),
                    ("coafile:use_LineLengthBear", "coafile:use_LineLengthBear"),
                    ("coafile:use_PyUnusedCodeBear", "coafile:use_PyUnusedCodeBear"),
                    ("coafile:use_RadonBear", "coafile:use_RadonBear"),
                    (
                        "coafile:use_PyCommentedCodeBear",
                        "coafile:use_PyCommentedCodeBear",
                    ),
                    ("coafile:use_PySafetyBear", "coafile:use_PySafetyBear"),
                    (
                        "coafile:use_PinRequirementsBear",
                        "coafile:use_PinRequirementsBear",
                    ),
                    ("coafile:use_PyImportSortBear", "coafile:use_PyImportSortBear"),
                ],
                max_length=500,
            ),
        )
    ]