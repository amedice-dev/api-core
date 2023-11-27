from django.contrib.postgres.fields import ArrayField
from django.db import models

from .types import OrgCategoryType, OrgDirectionsType
from doctors.models import Doctor


class Organisation(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=100)
    org_url = models.URLField(blank=True, null=True)
    ogr_category = models.CharField(max_length=40, choices=OrgCategoryType.choices)
    org_logo = models.ImageField(upload_to="org_logos", blank=True, null=True)
    org_local_adress = models.CharField(max_length=100, blank=True, null=True)
    org_local_landmark = models.CharField(max_length=100, blank=True, null=True)
    org_location = models.CharField(max_length=100, blank=True, null=True)
    org_local_phone = models.CharField(max_length=100)
    org_main_phone = models.CharField(max_length=100)
    org_legal_name = models.CharField(max_length=100, blank=True, null=True)
    org_working_hours = models.CharField(max_length=100, blank=True, null=True)
    org_site_link = models.URLField(blank=True, null=True)
    org_socials = models.ForeignKey(
        "OrgSocials",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="org_socials")
    org_photos = ArrayField(models.ImageField(upload_to="orgs"), blank=True, null=True)
    org_text_info = models.TextField(blank=True, null=True)
    org_directions = ArrayField(
        models.CharField(max_length=20, choices=OrgDirectionsType.choices),
        blank=True,
        null=True,
    )
    org_owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="org_owner"
    )

    org_admins = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="org_admins"
    )

    is_active = models.BooleanField(default=False)
    doctors_list = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    org_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    org_reviews = models.ForeignKey(
        "reviews.Review",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="org_reviews"
    )
    # org_views_counter = ...
    # org_clicks_counter = ...

    def __str__(self):
        return self.org_name


class OrgSocials(models.Model):
    whatsapp = models.CharField(max_length=100)
    viber = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    vkontakte = models.CharField(max_length=100)
    odnoklassniki = models.CharField(max_length=100)
    imo = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)


class OrgOwnersLink(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


class OrgAdminsLink(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)