# Generated by Django 5.0.4 on 2024-05-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctors", "0001_initial"),
        ("organisations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="organisations",
            field=models.ManyToManyField(
                related_name="doctors", to="organisations.organisation"
            ),
        ),
    ]