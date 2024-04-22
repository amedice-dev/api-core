from rest_framework import serializers

from .models import OrganisationReview, DoctorReview, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrgReviewSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()

    class Meta:
        model = OrganisationReview
        fields = ['id', 'organisation', 'review']

    def get_review(self, obj):
        if obj.review:
            return ReviewSerializer(obj.review).data


class DoctorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorReview
        fields = "__all__"
