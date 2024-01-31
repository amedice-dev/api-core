from django.db import models


class OrgSocials(models.Model):
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    viber = models.CharField(max_length=100, blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    vkontakte = models.CharField(max_length=100, blank=True, null=True)
    odnoklassniki = models.CharField(max_length=100, blank=True, null=True)
    imo = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
