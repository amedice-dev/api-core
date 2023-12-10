from rest_framework import serializers

from .models import Organisation


class OrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class OrganisationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ["org_name", "org_category", "org_directions", "org_local_phone"]
