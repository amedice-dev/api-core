from django.db import models


class DocDirectionsType(models.TextChoices):
    SURGEON = "Хирург"
    THERAPIST = "Терапевт"
    PEDIATRICIAN = "Педиатр"
    DENTIST = "Дантист"
    NEUROLOGIST = "Невролог"
    PSYCHIATRIST = "Психиатр"
    OPHTHALMOLOGIST = "Офтальмолог"
    OTOLARYNGOLOGIST = "Отоларинголог"
    GYNECOLOGIST = "Гинеколог"
    UROLOGIST = "Уролог"
    DERMATOLOGIST = "Дерматолог"
    VENEREOLOGIST = "Венеролог"
    ENDOCRINOLOGIST = "Эндокринолог"
    CARDIOLOGIST = "Кардиолог"
    ONCOLOGIST = "Онколог"
    ORTHOPEDIST = "Ортопед"
    PHYSIOTHERAPIST = "Физиотерапевт"
    COSMETOLOGIST = "Косметолог"

