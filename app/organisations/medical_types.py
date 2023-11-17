from django.db import models


class OrganisationType(models.TextChoices):
    HOSPITAL = "Больница"
    CLINIC = "Клиника"
    LABORATORY = "Лаборатория"
    DENTAL_CLINIC = "Стоматология"
    PHARMACY = "Аптека"
    MEDICAL_CENTER = "Медицинский центр"
    OPTICS = "Оптика"
    SANATORIUM = "Санаторий"
    MEDICAL_SCHOOL = "Медицинское учебное заведение"
    MEDICAL_EQUIPMENT = "Медицинское оборудование"


class SpecialityType(models.TextChoices):
    SURGEON = "Хирург"
    THERAPIST = "Терапевт"
    PEDIATRICIAN = "Педиатр"
    DENTIST = "Дантист"
    NEUROLOGIST = "Невролог"
    PSYCHIATRIST = "Психиатр"
    OPHTHALMOLOGIST = "Офтальмолог"


class ServiceType(models.TextChoices):
    SURGERY = "Хирургия"
    THERAPY = "Терапия"
    PEDIATRICS = "Педиатрия"
    DENTISTRY = "Стоматология"
    NEUROLOGY = "Неврология"
    PSYCHIATRY = "Психиатрия"
    OPHTHALMOLOGY = "Офтальмология"
    XRAY = "Рентген"
    ULTRASOUND = "УЗИ"
    MRI = "МРТ"
    CT = "КТ"
    LABORATORY = "Лаборатория"
    PHYSIOTHERAPY = "Физиотерапия"
    MASSAGE = "Массаж"
    COSMETOLOGY = "Косметология"
