from django.contrib.postgres.fields import ArrayField
from django.db import models

from .types import DocDirectionsType
from reviews.models import Review


class Doctor(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_first_name = models.CharField(max_length=100)
    doc_last_name = models.CharField(max_length=100)
    doc_middle_name = models.CharField(max_length=100)
    doc_directions = ArrayField(
        models.CharField(max_length=20, choices=DocDirectionsType.choices),
        blank=True,
        null=True,
    )
    doc_avatar = models.ImageField(upload_to="doctors", blank=True)
    doc_rating = models.DecimalField(max_digits=2, decimal_places=1)
    doc_reviews = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="doctor_reviews",
    )
