# Generated by Django 4.2.6 on 2024-01-22 21:18

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrgAdminsLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
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
                    "org_logo",
                    models.ImageField(blank=True, null=True, upload_to="org_logos"),
                ),
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
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("org_site_link", models.URLField(blank=True, null=True)),
                (
                    "org_photos",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.ImageField(upload_to="orgs"),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "org_text_info",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "org_rating",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=2, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrgSocials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("whatsapp", models.CharField(max_length=100)),
                ("viber", models.CharField(max_length=100)),
                ("telegram", models.CharField(max_length=100)),
                ("instagram", models.CharField(max_length=100)),
                ("facebook", models.CharField(max_length=100)),
                ("vkontakte", models.CharField(max_length=100)),
                ("odnoklassniki", models.CharField(max_length=100)),
                ("imo", models.CharField(max_length=100)),
                ("youtube", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="OrgOwnersLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organisations.organisation",
                    ),
                ),
            ],
        ),
    ]
