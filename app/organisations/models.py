from django.contrib.postgres.fields import ArrayField
from django.db import models

from catalog.models import OrgCategory, OrgDirection
from doctors.models import Doctor
from reviews.models import Review
from socials.models import OrgSocials


class Organisation(models.Model):
    org_id = models.AutoField(primary_key=True, db_index=True)
    org_name = models.CharField(max_length=100)
    org_slug = models.SlugField(max_length=130, unique=True, db_index=True)
    org_category = models.ForeignKey(OrgCategory, on_delete=models.PROTECT, blank=True)
    org_directions = models.ManyToManyField(OrgDirection, blank=True)
    org_local_phone = models.CharField(max_length=100)
    org_main_phone = models.CharField(max_length=100, blank=True, null=True)
    org_url = models.URLField(blank=True, null=True)
    org_logo = models.ImageField(upload_to="org_logos", blank=True, null=True)
    org_local_address = models.CharField(max_length=100, blank=True, null=True)
    org_local_landmark = models.CharField(max_length=100, blank=True, null=True)
    org_location = models.CharField(max_length=100, blank=True, null=True)
    org_legal_name = models.CharField(max_length=100, blank=True, null=True)
    org_working_hours = models.JSONField(blank=True, null=True)
    org_site_link = models.URLField(blank=True, null=True)
    org_socials = models.ForeignKey(OrgSocials, on_delete=models.SET_NULL, blank=True, null=True)
    org_photos = ArrayField(models.ImageField(upload_to="orgs"), blank=True, null=True)
    org_text_info = models.CharField(max_length=1000, blank=True, null=True)
    org_owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="org_owner",
    )

    org_admins = models.ManyToManyField(
        "users.User", blank=True, related_name="org_admins"
    )

    is_active = models.BooleanField(default=False)
    doctors_list = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True
    )
    org_rating = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True
    )
    org_reviews = models.ManyToManyField(
        "reviews.Review",
        blank=True,
        related_name="org_reviews",
    )
    updated_at = models.DateTimeField(auto_now=True)
    # org_views_counter = ...
    # org_clicks_counter = ...


class OrgOwnersLink(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


class OrgAdminsLink(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


class UserReviewLink(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
