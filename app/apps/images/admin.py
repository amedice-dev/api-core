from django.contrib import admin
from django.utils.html import mark_safe

from apps.images.models import OrgPhoto, OrgLogo, DoctorAvatar, UserAvatar


@admin.register(OrgPhoto)
class OrgPhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'org_id', 'image_preview', 'uploaded_at')

    def image_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" style="max-width:100px; max-height:100px" />'.format(url=obj.image.url))
        except Exception as e:
            return str(e)

    image_preview.short_description = 'Image Preview'


@admin.register(OrgLogo)
class OrgLogoAdmin(admin.ModelAdmin):
    list_display = ('image', 'org_id', 'image_preview', 'uploaded_at')

    def image_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" style="max-width:100px; max-height:100px" />'.format(url=obj.image.url))
        except Exception as e:
            return str(e)

    image_preview.short_description = 'Image Preview'


@admin.register(DoctorAvatar)
class DoctorAvatarAdmin(admin.ModelAdmin):
    list_display = ('image', 'doc_id', 'image_preview', 'uploaded_at')

    def image_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" style="max-width:100px; max-height:100px" />'.format(url=obj.image.url))
        except Exception as e:
            return str(e)

    image_preview.short_description = 'Image Preview'


@admin.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    list_display = ('image', 'user_id', 'image_preview', 'uploaded_at')

    def image_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" style="max-width:100px; max-height:100px" />'.format(url=obj.image.url))
        except Exception as e:
            return str(e)

    image_preview.short_description = 'Image Preview'
