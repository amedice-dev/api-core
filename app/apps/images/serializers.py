from rest_framework import serializers
from .models import Image


class OrgPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class OrgLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class DoctorAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
