from rest_framework import serializers

from .models import OrgSocials


class OrgSocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgSocials
        fields = "__all__"
