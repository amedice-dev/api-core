from rest_framework import serializers
from django.db import models

from .models import User, UserRole


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    user_role = serializers.ChoiceField(choices=UserRole.choices, write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "user_phone",
            "user_role",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
