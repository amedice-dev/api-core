from django.db import models

from apps.users.models import User
from apps.organisations.models import Organisation
from apps.doctors.models import Doctor


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_grade = models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)


class OrganisationReview(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='org_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class DoctorReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
