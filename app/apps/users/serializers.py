from rest_framework import serializers

from .models import User, UserRole


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    user_role = serializers.ChoiceField(
        choices=UserRole.choices, write_only=True, required=False, allow_null=True
    )
    groups = serializers.SlugRelatedField(many=True, read_only=True, slug_field="id")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_phone",
            "user_role",
            "groups",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
