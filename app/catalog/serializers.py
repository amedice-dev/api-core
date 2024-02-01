from rest_framework import serializers

from catalog.models import OrgCategory, OrgDirection


class OrgCategoryWithCountSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgCategory
        fields = ["category_id", "name", "slug", "type", "count"]


class OrgCategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgCategory
        fields = ["category_id", "name", "slug", "type", "page_content"]


class OrgDirectionSerializer(serializers.ModelSerializer):
    direction_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgDirection
        fields = ["direction_id", "name", "slug"]


class CategoryPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgCategory
        fields = ["page_content"]
