from apps.doctors.serializers import DoctorsSerializer
from apps.images.serializers import OrgLogoSerializer, OrgPhotoSerializer
from apps.reviews.serializers import OrgReviewSerializer
from apps.socials.serializers import OrgSocialsSerializer
from rest_framework import serializers

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


class OrganisationsSerializer(BaseOrganisationSerializer):
    org_text_info_short = serializers.SerializerMethodField()
    org_category = serializers.SerializerMethodField()
    org_directions = serializers.SerializerMethodField()
    org_logo = serializers.SerializerMethodField()

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

    def get_org_logo(self, obj) -> dict | None:
        logo = obj.images.filter(content_type="org_logo").first()
        if logo:
            return OrgLogoSerializer(logo).data
        return None


class OrganisationUpdateSerializer(serializers.ModelSerializer):
    org_working_hours = serializers.JSONField(validators=[validate_working_hours])
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Organisation
        fields = [
            "org_id",
            "org_name",
            "org_slug",
            "org_local_phone",
            "org_main_phone",
            "org_url",
            "org_local_address",
            "org_local_landmark",
            "org_location",
            "org_legal_name",
            "org_working_hours",
            "org_site_link",
            "org_text_info",
            "is_active",
            "org_socials",
            "org_category",
            "org_directions",
            "updated_at",
        ]


class OrganisationDetailSerializer(BaseOrganisationSerializer):
    org_category = serializers.SerializerMethodField()
    org_directions = serializers.SerializerMethodField()
    org_socials = serializers.SerializerMethodField()
    org_logo = serializers.SerializerMethodField()
    org_photos = serializers.SerializerMethodField()
    org_reviews = serializers.SerializerMethodField()
    doctors_list = serializers.SerializerMethodField()
    updated_at = serializers.DateTimeField(read_only=True)

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
            "updated_at",
        ]

    def get_org_socials(self, obj) -> list[dict]:
        if obj.org_socials:
            return OrgSocialsSerializer(obj.org_socials).data

    def get_org_logo(self, obj) -> dict | None:
        logo = obj.images.filter(content_type="org_logo").first()
        if logo:
            return OrgLogoSerializer(logo).data
        return None

    def get_org_photos(self, obj) -> list[dict]:
        photos = obj.images.filter(content_type="org_photo").order_by("order")
        if photos.exists():
            return OrgPhotoSerializer(photos, many=True).data
        return []

    def get_org_reviews(self, obj) -> list[dict]:
        if obj.org_reviews:
            return OrgReviewSerializer(obj.org_reviews.all(), many=True).data

    def get_doctors_list(self, obj) -> list[dict]:
        if obj.doctors:
            return DoctorsSerializer(obj.doctors.all(), many=True).data
