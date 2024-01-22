from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import connection
from catalog.models import OrgCategory, OrgDirection


org_categories = [
    {"name": "Медицинский центр", "slug": "med_center", "type": "private"},
    {"name": "Лаборатория", "slug": "laboratory", "type": "private"},
    {"name": "Стоматологическая клиника", "slug": "dental_clinic", "type": "private"},
    {"name": "Диагностический центр", "slug": "diagnostic_center", "type": "private"},
    {"name": "Офтальмологическая клиника", "slug": "eye_clinic", "type": "private"},
    {"name": "Детская клиника", "slug": "kids_clinic", "type": "private"},
    {
        "name": "Косметологический центр",
        "slug": "cosmetology_center",
        "type": "private",
    },
    {"name": "Госпиталь", "slug": "gos_hospital", "type": "public"},
    {"name": "Амбулатория", "slug": "gos_ambulatory", "type": "public"},
    {"name": "Детский госпиталь", "slug": "gos_kids_hospital", "type": "public"},
    {"name": "Госполиклиника", "slug": "gos_polyclinic", "type": "public"},
    {
        "name": "Государственная стоматологическая поликлиника",
        "slug": "gos_dental_polyclinic",
        "type": "public",
    },
    {
        "name": "Государственный роддом",
        "slug": "gos_maternity_hospital",
        "type": "public",
    },
    {"name": "Диспансер", "slug": "gos_dispensary", "type": "public"},
]

org_directions = [
    {"name": "Урология", "slug": "urology"},
    {"name": "Терапия", "slug": "therapy"},
    {"name": "Стоматология", "slug": "dentistry"},
    {"name": "Дерматология", "slug": "dermatology"},
    {"name": "Неврология", "slug": "neurology"},
    {"name": "Косметология", "slug": "cosmetology"},
    {"name": "Венерология", "slug": "venereology"},
    {"name": "Ортопедия", "slug": "orthopedics"},
    {"name": "Физиотерапия", "slug": "physiotherapy"},
    {"name": "Хирургия", "slug": "surgery"},
    {"name": "Эндокринология", "slug": "endocrinology"},
    {"name": "Онкология", "slug": "oncology"},
    {"name": "Педиатрия", "slug": "pediatrics"},
    {"name": "Кардиология", "slug": "cardiology"},
    {"name": "Отоларингология", "slug": "oto_rhino_laryngology"},
    {"name": "Психиатрия", "slug": "psychiatry"},
    {"name": "Офтальмология", "slug": "ophthalmology"},
    {"name": "Гинекология", "slug": "gynecology"},
]


@receiver(post_migrate)
def create_org_categories(**kwargs):
    # Create OrgCategory objects only if the table exists in the database
    if OrgCategory._meta.db_table in connection.introspection.table_names():
        # Check if OrgCategory objects already exist
        for category in org_categories:
            OrgCategory.objects.get_or_create(
                name=category["name"], slug=category["slug"], type=category["type"]
            )


@receiver(post_migrate)
def create_org_directions(**kwargs):
    # Create OrgDirection objects only if the table exists in the database
    if OrgDirection._meta.db_table in connection.introspection.table_names():
        # Check if OrgDirection objects already exist
        for direction in org_directions:
            OrgDirection.objects.get_or_create(
                name=direction["name"], slug=direction["slug"]
            )
