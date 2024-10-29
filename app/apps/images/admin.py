from apps.images.models import Image
from django.contrib import admin
from django.utils.html import mark_safe


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "content_type",
        "object_id",
        "image_preview",
        "uploaded_at",
    )

    def object_id(self, obj):
        if obj.content_type == "org_photo" or obj.content_type == "org_logo":
            return obj.org.org_id if obj.org else "No Org"
        elif obj.content_type == "doctor_avatar":
            return obj.doctor.doc_id if obj.doctor else "No Doctor"
        elif obj.content_type == "user_avatar":
            return obj.user.id if obj.user else "No User"
        return "Unknown"

    object_id.short_description = "Object ID"

    def image_preview(self, obj):
        try:
            return mark_safe(
                '<img src="{url}" style="max-width:100px; max-height:100px" />'.format(
                    url=obj.image.url
                )
            )
        except Exception as e:
            return str(e)

    image_preview.short_description = "Image Preview"
