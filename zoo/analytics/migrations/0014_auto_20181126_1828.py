# Generated by Django 2.1.3 on 2018-11-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("analytics", "0013_dependency_license")]

    operations = [
        migrations.AlterField(
            model_name="dependency",
            name="license",
            field=models.CharField(blank=True, max_length=10000, null=True),
        )
    ]
