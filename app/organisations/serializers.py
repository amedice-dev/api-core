from rest_framework import serializers
from django.utils.text import slugify
from django.db.models import Max
from transliterate import translit

from .models import Organisation
from .types import OrgCategory, OrgDirection


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
        # Adding org_id only with the GET method
        ret = super().to_representation(instance)
        if self.context["request"].method == "GET":
            ret["org_id"] = instance.org_id
        return ret

    def save(self, **kwargs):
        # Generating org_slug from transliterated org_name and org_id
        org_name = self.validated_data["org_name"]
        max_org_id = Organisation.objects.aggregate(Max("org_id"))["org_id__max"] or 0
        org_id = max_org_id + 1
        org_name_translit = translit(org_name, "ru", reversed=True)
        org_slug = slugify(f"{org_id}_{org_name_translit}")
        self.validated_data["org_slug"] = org_slug.replace("-", "_")

        return super().save(**kwargs)


class OrgCategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrgCategory
        fields = ["category_id", "name", "slug", "type", "count"]


class OrgDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgDirection
        fields = ["direction_id", "name", "slug"]


class OrganisationsSerializer(serializers.ModelSerializer):
    org_text_info_short = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_slug",
            "org_name",
            "org_category",
            "org_directions",
            "org_local_adress",
            "org_logo",
            "org_text_info_short",
        ]

    def get_org_text_info_short(self, obj):
        return obj.org_text_info[:200] + "..." if obj.org_text_info else None


class OrganisationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"
