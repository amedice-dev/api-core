from rest_framework import serializers
from django.utils.text import slugify
from django.db.models import Max
from transliterate import translit

from socials.models import OrgSocials
from users.models import User
from .models import Organisation
from .validators import validate_working_hours


class BaseOrganisationSerializer(serializers.ModelSerializer):
    def get_org_category(self, obj) -> dict | None:
        if obj.org_category:
            return {
                "id": obj.org_category.category_id,
                "name": obj.org_category.name,
                "slug": obj.org_category.slug,
            }
        return None

    def get_org_directions(self, obj) -> list[dict]:
        return [
            {
                "id": direction.direction_id,
                "name": direction.name,
                "slug": direction.slug,
            }
            for direction in obj.org_directions.all()
        ]

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


class OrganisationsSerializer(BaseOrganisationSerializer):
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


class OrganisationUpdateSerializer(serializers.ModelSerializer):
    org_working_hours = serializers.JSONField(validators=[validate_working_hours])

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_name",
            "org_slug",
            "org_local_phone",
            "org_main_phone",
            "org_logo",
            "org_url",
            "org_local_address",
            "org_local_landmark",
            "org_location",
            "org_legal_name",
            "org_working_hours",
            "org_site_link",
            "org_photos",
            "org_text_info",
            "is_active",
            "org_socials",
            "doctors_list",
            "org_category",
            "org_directions",
        ]


class OrganisationDetailSerializer(BaseOrganisationSerializer):
    org_socials = serializers.SerializerMethodField(read_only=True)
    org_category = serializers.SerializerMethodField()
    org_directions = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_name",
            "org_slug",
            "org_local_phone",
            "org_main_phone",
            "org_logo",
            "org_url",
            "org_local_address",
            "org_local_landmark",
            "org_location",
            "org_legal_name",
            "org_working_hours",
            "org_site_link",
            "org_photos",
            "org_text_info",
            "is_active",
            "org_rating",
            "org_category",
            "org_directions",
            "org_socials",
            "doctors_list",
            "org_reviews",
        ]

    def get_org_socials(self, obj):

        if obj.org_socials:
            org_socials_instance = OrgSocials.objects.get(id=obj.org_socials.id)
            socials_data = {
                "whatsapp": org_socials_instance.whatsapp,
                "viber": org_socials_instance.viber,
                "telegram": org_socials_instance.telegram,
                "instagram": org_socials_instance.instagram,
                "facebook": org_socials_instance.facebook,
                "vkontakte": org_socials_instance.vkontakte,
                "odnoklassniki": org_socials_instance.odnoklassniki,
                "imo": org_socials_instance.imo,
                "youtube": org_socials_instance.youtube,
            }
            return socials_data
