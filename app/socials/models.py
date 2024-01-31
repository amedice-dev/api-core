from django.db import models


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
