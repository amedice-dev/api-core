# Generated by Django 5.1.2 on 2024-10-29 12:02

import apps.organisations.defaults
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "org_id",
                    models.AutoField(db_index=True, primary_key=True, serialize=False),
                ),
                ("org_name", models.CharField(max_length=100)),
                ("org_slug", models.SlugField(max_length=130, unique=True)),
                ("org_local_phone", models.CharField(max_length=100)),
                (
                    "org_main_phone",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("org_url", models.URLField(blank=True, null=True)),
                (
                    "org_local_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "org_local_landmark",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "org_location",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "org_legal_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "org_working_hours",
                    models.JSONField(
                        blank=True,
                        default=apps.organisations.defaults.default_working_hours,
                        null=True,
                    ),
                ),
                ("org_site_link", models.URLField(blank=True, null=True)),
                (
                    "org_text_info",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "org_rating",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=2, null=True
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
