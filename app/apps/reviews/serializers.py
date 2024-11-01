from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def get_review(self, obj):
        if obj.review:
            return ReviewSerializer(obj.review).data
