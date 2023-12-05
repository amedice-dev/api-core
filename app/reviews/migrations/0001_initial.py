# Generated by Django 4.2.6 on 2023-12-05 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("review_id", models.AutoField(primary_key=True, serialize=False)),
                ("review_text", models.TextField()),
                ("review_grade", models.IntegerField()),
                ("publication_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserReviewLink",
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
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reviews.review"
                    ),
                ),
            ],
        ),
    ]
