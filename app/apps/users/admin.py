from apps.images.models import Image
from django import forms
from django.contrib import admin
from django.utils.html import mark_safe

from .models import User


class UserAvatarInline(admin.TabularInline):
    model = Image
    extra = 0
    max_num = 1
    readonly_fields = ("image_preview",)
    exclude = ("doctor", "org", "order")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user__isnull=False, content_type="user_avatar")

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            kwargs["choices"] = [("user_avatar", "User Avatar")]
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{url}" style="max-width:100px; max-height:100px;" />'.format(
                    url=obj.image.url
                )
            )
        return "No Image"

    image_preview.short_description = "Image Preview"


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = (
        "id",
        "email",
        "user_phone",
        "is_email_verified",
        "is_phone_verified",
        "is_active",
        "last_login",
    )
    search_fields = ["email", "user_phone"]
    list_filter = ["is_active", "is_email_verified", "is_phone_verified"]
    inlines = [UserAvatarInline]


admin.site.register(User, UserAdmin)
