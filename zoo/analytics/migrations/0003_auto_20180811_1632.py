# Generated by Django 2.0.7 on 2018-08-11 16:32

from django.db import migrations
import zoo.analytics.models


class Migration(migrations.Migration):

    dependencies = [("analytics", "0002_auto_20180808_1252")]

    operations = [
        migrations.AlterField(
            model_name="dependency",
            name="name",
            field=zoo.analytics.models.NameField(max_length=1000),
        )
    ]