from django.contrib.postgres.fields import ArrayField
from django.db import models

from organisations.models import SpecialityType


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speciality = ArrayField(
        models.CharField(max_length=20, choices=SpecialityType.choices),
        blank=True,
        null=True,
    )
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
