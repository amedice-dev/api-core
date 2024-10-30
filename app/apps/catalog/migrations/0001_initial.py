# Generated by Django 5.1.2 on 2024-10-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrgCategory",
            fields=[
                (
                    "category_id",
                    models.AutoField(db_index=True, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("private", "Private"), ("public", "Public")],
                        db_index=True,
                        max_length=40,
                    ),
                ),
                ("page_content", models.JSONField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Org category",
                "verbose_name_plural": "Org categories",
            },
        ),
        migrations.CreateModel(
            name="OrgDirection",
            fields=[
                (
                    "direction_id",
                    models.AutoField(db_index=True, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
