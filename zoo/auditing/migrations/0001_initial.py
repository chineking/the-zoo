# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import zoo.auditing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            (
                                "repo_config:require_approvals",
                                "repo_config:require_approvals",
                            ),
                            ("repo_config:use_rebase", "repo_config:use_rebase"),
                            (
                                "repo_config:reset_approvals_on_push",
                                "repo_config:reset_approvals_on_push",
                            ),
                            (
                                "repo_config:block_on_discussions",
                                "repo_config:block_on_discussions",
                            ),
                            (
                                "repo_config:block_on_ci_failure",
                                "repo_config:block_on_ci_failure",
                            ),
                            ("repo_config:autocancel_ci", "repo_config:autocancel_ci"),
                            (
                                "repo_config:protect_master",
                                "repo_config:protect_master",
                            ),
                        ],
                        max_length=500,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("new", "new"), ("fixed", "fixed")],
                        default=zoo.auditing.models.Issue.Status("new"),
                        max_length=100,
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        )
    ]
