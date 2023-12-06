# Generated by Django 4.2.6 on 2023-12-07 22:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("doc_id", models.AutoField(primary_key=True, serialize=False)),
                ("doc_first_name", models.CharField(max_length=100)),
                ("doc_last_name", models.CharField(max_length=100)),
                ("doc_middle_name", models.CharField(max_length=100)),
                (
                    "doc_directions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("Хирург", "Surgeon"),
                                ("Терапевт", "Therapist"),
                                ("Педиатр", "Pediatrician"),
                                ("Дантист", "Dentist"),
                                ("Невролог", "Neurologist"),
                                ("Психиатр", "Psychiatrist"),
                                ("Офтальмолог", "Ophthalmologist"),
                                ("Отоларинголог", "Otolaryngologist"),
                                ("Гинеколог", "Gynecologist"),
                                ("Уролог", "Urologist"),
                                ("Дерматолог", "Dermatologist"),
                                ("Венеролог", "Venereologist"),
                                ("Эндокринолог", "Endocrinologist"),
                                ("Кардиолог", "Cardiologist"),
                                ("Онколог", "Oncologist"),
                                ("Ортопед", "Orthopedist"),
                                ("Физиотерапевт", "Physiotherapist"),
                                ("Косметолог", "Cosmetologist"),
                            ],
                            max_length=20,
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("doc_avatar", models.ImageField(blank=True, upload_to="doctors")),
                ("doc_rating", models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
