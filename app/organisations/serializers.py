from rest_framework import serializers
from django.utils.text import slugify
from django.db.models import Max
from transliterate import translit

from .models import Organisation


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
        org_slug = slugify(f"{org_id}-{org_name_translit}")
        self.validated_data["org_slug"] = org_slug

        return super().save(**kwargs)


class OrganisationsSerializer(serializers.ModelSerializer):
    org_text_info_short = serializers.SerializerMethodField()
    org_category = serializers.SerializerMethodField()
    org_directions = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_slug",
            "org_name",
            "org_category",
            "org_directions",
            "org_local_address",
            "org_logo",
            "org_text_info_short",
        ]

    def get_org_text_info_short(self, obj) -> str | None:
        return obj.org_text_info[:200] + "..." if obj.org_text_info else None

    def get_org_category(self, obj) -> str | None:
        result = {
            "id": obj.org_category.category_id,
            "name": obj.org_category.name,
            "slug": obj.org_category.slug,
        }
        return result if obj.org_category else ""

    def get_org_directions(self, obj) -> list[dict]:
        result = [
            {
                "id": direction.direction_id,
                "name": direction.name,
                "slug": direction.slug,
            }
            for direction in obj.org_directions.all()
        ]
        return result


class OrganisationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"
