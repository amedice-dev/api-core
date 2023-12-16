from rest_framework import serializers

from .models import Organisation
from .types import OrgCategory, OrgDirection


class OrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class OrganisationPostSerializer(serializers.ModelSerializer):
    # Defining org_id as a read-only field
    org_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_name",
            "org_category",
            "org_directions",
            "org_local_phone",
        ]

    def to_representation(self, instance):
        # Добавляем org_id только при методе GET
        ret = super().to_representation(instance)
        if self.context["request"].method == "GET":
            ret["org_id"] = instance.org_id
        return ret


class OrgCategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgCategory
        fields = ["category_id", "name", "slug", "type", "count"]


class OrgDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgDirection
        fields = ["direction_id", "name", "slug"]
