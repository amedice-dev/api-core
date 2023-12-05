from django.db import models


class OrgCategoryType(models.TextChoices):
    MED_CENTER = "Медицинский центр"
    LABORATORY = "Лаборатория"
    DENTAL_CLINIC = "Стоматология"
    DIAGNOSTIC_CENTER = "Диагностический центр"
    EYE_CLINIC = "Офтальмологическая клиника"
    KIDS_CLINIC = "Детская клиника"
    COSMETOLOGY_CENTER = "Косметологический центр"

    GOS_HOSPITAL = "Больница"
    GOS_AMBULATORY = "Амбулатория"
    GOS_KIDS_HOSPITAL = "Детская больница"
    GOS_POLYCLINIC = "Поликлиника"
    GOS_DENTAL_POLYCLINIC = "Стоматологическая поликлиника"
    GOS_MATERNITY_HOSPITAL = "Роддом"
    GOS_DISPENSARY = "Диспансер"


class OrgDirectionsType(models.TextChoices):
    UROLOGY = "Урология"
    THERAPY = "Терапия"
    DENTISTRY = "Стоматология"
    DERMATOLOGY = "Дерматология"
    NEUROLOGY = "Неврология"
    COSMETOLOGY = "Косметология"
    VENEREOLOGY = "Венерология"
    ORTOPEDICS = "Ортопедия"
    PHYSIOTHERAPY = "Физиотерапия"
    SURGERY = "Хирургия"
    ENDOCRINOLOGY = "Эндокринология"
    ONCOLOGY = "Онкология"
    PEDIATRICS = "Педиатрия"
    CARDIOLOGY = "Кардиология"
    OTO_RHINO_LARYNGOLOGY = "Отоларингология"
    PSYCHIATRY = "Психиатрия"
    OPHTHALMOLOGY = "Офтальмология"
    GYNECOLOGY = "Гинекология"
