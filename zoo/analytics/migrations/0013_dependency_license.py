# Generated by Django 2.1.3 on 2018-11-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("analytics", "0012_depusage_bigint_version")]

    operations = [
        migrations.AddField(
            model_name="dependency",
            name="license",
            field=models.CharField(blank=True, max_length=100, null=True),
        )
    ]
