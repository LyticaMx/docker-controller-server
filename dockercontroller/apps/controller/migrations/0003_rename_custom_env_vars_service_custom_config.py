# Generated by Django 3.2.6 on 2021-08-19 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("controller", "0002_alter_service_version"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="custom_env_vars",
            new_name="custom_config",
        ),
    ]
