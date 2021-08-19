# Generated by Django 3.2.6 on 2021-08-19 17:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("controller", "0005_auto_20210819_1721"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicedefinition",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicedefinition",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
