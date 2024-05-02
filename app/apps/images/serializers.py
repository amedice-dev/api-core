from rest_framework import serializers
from .models import OrgPhoto, OrgLogo, DoctorAvatar, UserAvatar


class OrgPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgPhoto
        fields = ['id', 'image']


class OrgLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLogo
        fields = '__all__'


class DoctorAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvatar
        fields = '__all__'


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAvatar
        fields = '__all__'
