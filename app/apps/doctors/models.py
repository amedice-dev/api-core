from apps.organisations.models import Organisation
from django.contrib.postgres.fields import ArrayField
from django.db import models

from .types import DocDirectionsType


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
    doc_rating = models.DecimalField(max_digits=2, decimal_places=1)

    organisations = models.ManyToManyField(Organisation, related_name="doctors")
