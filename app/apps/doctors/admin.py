from apps.images.models import Image
from django import forms
from django.contrib import admin
from django.utils.html import mark_safe

from .models import Doctor


class DoctorAvatarInline(admin.TabularInline):
    model = Image
    extra = 0
    max_num = 1
    readonly_fields = ("image_preview",)
    exclude = ("user", "org")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(doctor__isnull=False, content_type="doctor_avatar")

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            kwargs["choices"] = [("doctor_avatar", "Doctor Avatar")]
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


class DoctorAdminForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorAdmin(admin.ModelAdmin):
    form = DoctorAdminForm
    list_display = (
        "doc_id",
        "doc_last_name",
        "doc_first_name",
        "doc_middle_name",
        "doc_rating",
    )
    search_fields = ["doc_first_name", "doc_last_name"]
    list_filter = ["doc_rating"]
    inlines = [DoctorAvatarInline]


admin.site.register(Doctor, DoctorAdmin)
