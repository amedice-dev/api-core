import os
import uuid

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


def generate_image_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("images", filename)


class ImageType(models.TextChoices):
    ORG_PHOTO = "org_photo", "Organisation Photo"
    ORG_LOGO = "org_logo", "Organisation Logo"
    DOC_AVATAR = "doctor_avatar", "Doctor Avatar"
    USER_AVATAR = "user_avatar", "User Avatar"


class Image(models.Model):
    image = models.ImageField(upload_to=generate_image_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=20, choices=ImageType.choices)
    org = models.ForeignKey(
        "organisations.Organisation",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="images",
    )
    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="avatar",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="avatar",
    )
    order = models.PositiveSmallIntegerField(default=0, blank=True, null=True)


@receiver(post_delete, sender=Image)
def delete_org_media_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
