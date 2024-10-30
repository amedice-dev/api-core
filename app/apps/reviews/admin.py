from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_text",
        "user_email",
        "type",
        "object_id",
        "created_at",
        "updated_at",
    )

    def object_id(self, obj):
        if obj.type == "org_review":
            return obj.organisation.org_id if obj.organisation else "No Org"
        elif obj.content_type == "doc_review":
            return obj.doctor.doc_id if obj.doctor else "No Doctor"
        return "Unknown"

    def short_text(self, obj):
        return obj.text[:45] + "..."

    def user_email(self, obj):
        return obj.user.email

    object_id.short_description = "Object ID"
