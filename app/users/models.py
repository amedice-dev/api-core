from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
)
from django.db import models

from users.groups import create_groups


create_groups()


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")

        user_role = extra_fields.pop("user_role", None)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        if user_role:
            group = Group.objects.filter(name=user_role).first()
            if group:
                group.user_set.add(user)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class UserRole(models.TextChoices):
    ADMINISTRATORS = "Administrators"
    OWNERS = "Owners"
    VISITORS = "Visitors"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=100)
    user_avatar = models.ImageField(upload_to="users_avatars", blank=True, null=True)

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    user_reviews = models.ForeignKey(
        "reviews.Review",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_reviews",
    )
    organisations_list = models.ForeignKey(
        "organisations.Organisation",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="organisations_list",
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "user_phone"]
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email
