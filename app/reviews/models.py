from django.db import models

from users.models import User


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_grade = models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)
