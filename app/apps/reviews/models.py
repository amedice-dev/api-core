from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.models.mixins import TimestampMixin
from apps.users.models import User
from apps.doctors.models import Doctor
from apps.organisations.models import Organisation


class ReviewType(models.TextChoices):
    ORG_REVIEW = 'org_review', 'Organisation Review'
    DOC_REVIEW = 'doc_review', 'Doctor Review'


class Review(TimestampMixin, models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField(max_length=400)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    type = models.CharField(max_length=20, choices=ReviewType.choices)
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True, blank=True, related_name="reviews"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, null=True, blank=True, related_name="reviews"
    )
