from django.db import models

class OrgCategoryType(models.TextChoices):
    PRIVATE = "private"
    PUBLIC = "public"


class OrgCategory(models.Model):
    category_id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    type = models.CharField(
        max_length=40, choices=OrgCategoryType.choices, db_index=True
    )
    page_content = models.JSONField(blank=True, null=True)


class OrgDirection(models.Model):
    direction_id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
