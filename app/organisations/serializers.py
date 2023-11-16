from rest_framework import serializers

from .models import Organisation


class OrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"
