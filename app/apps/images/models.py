import os
import uuid
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


def generate_org_photo_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("orgs_photos", filename)


def generate_org_logo_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("orgs_logos", filename)


def generate_doctor_avatar_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("doctors_avatars", filename)


def generate_user_avatar_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("users_avatars", filename)


class BaseImageModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class OrgPhoto(BaseImageModel):
    image = models.ImageField(upload_to=generate_org_photo_filename)
    org_id = models.ForeignKey("organisations.Organisation", related_name="photos", on_delete=models.CASCADE)


class OrgLogo(BaseImageModel):
    image = models.ImageField(upload_to=generate_org_logo_filename)
    org_id = models.OneToOneField("organisations.Organisation", related_name="org_logo", on_delete=models.CASCADE)


class DoctorAvatar(BaseImageModel):
    image = models.ImageField(upload_to=generate_doctor_avatar_filename)
    doc_id = models.OneToOneField("doctors.Doctor", related_name="doctor_avatar", on_delete=models.CASCADE)


class UserAvatar(BaseImageModel):
    image = models.ImageField(upload_to=generate_user_avatar_filename)
    user_id = models.OneToOneField("users.User", related_name="user_avatar", on_delete=models.CASCADE)


@receiver(post_delete, sender=OrgPhoto)
@receiver(post_delete, sender=OrgLogo)
@receiver(post_delete, sender=DoctorAvatar)
@receiver(post_delete, sender=UserAvatar)
def delete_org_media_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
