from django.contrib.postgres.fields import ArrayField
from django.db import models

from .defaults import DEFAULT_DESCRIPTION
from .medical_types import OrganisationType, SpecialityType, ServiceType
from doctors.models import Doctor


class Organisation(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(
        max_length=40,
        choices=OrganisationType.choices,
        db_index=True,
        blank=False,
    )
    description = models.CharField(max_length=1000, default=DEFAULT_DESCRIPTION)
    services = ArrayField(
        models.CharField(max_length=20, choices=ServiceType.choices),
        blank=True,
        null=True,
    )
    doctors_speciality = ArrayField(
        models.CharField(max_length=20, choices=SpecialityType.choices),
        blank=True,
        null=True,
    )
    doctors = models.ManyToManyField(Doctor, blank=True, null=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
