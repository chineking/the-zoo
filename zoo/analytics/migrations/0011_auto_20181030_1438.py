# Generated by Django 2.1.1 on 2018-10-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("analytics", "0010_auto_20180927_1919")]

    operations = [
        migrations.AlterField(
            model_name="dependencyusage",
            name="major_version",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dependencyusage",
            name="minor_version",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dependencyusage",
            name="patch_version",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]