from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
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


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=100, blank=True, null=True)
    # user_group = ...
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    user_avatar = models.ImageField(upload_to="users_avatars", blank=True, null=True)

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
