# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("auditing", "0004b_auto_20171206_1432")]

    operations = [migrations.RemoveField(model_name="issue", name="kind")]