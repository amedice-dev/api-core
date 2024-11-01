from django.contrib.auth.models import Group
from django.db import connection
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_groups(**kwargs):
    # Create groups only if table auth_group exists in database
    if "auth_group" in connection.introspection.table_names():
        owners_group, created = Group.objects.get_or_create(name="Owners")
        admins_group, created = Group.objects.get_or_create(name="Administrators")
        visitors_group, created = Group.objects.get_or_create(name="Visitors")
