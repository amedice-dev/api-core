from rest_framework import serializers

from catalog.models import OrgCategory, OrgDirection


class OrgCategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgCategory
        fields = ["category_id", "name", "slug", "type", "count"]


class OrgDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgDirection
        fields = ["direction_id", "name", "slug"]
