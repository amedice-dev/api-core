from rest_framework import serializers

from organisations.models import MedicalInstitution


class OrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = "__all__"
