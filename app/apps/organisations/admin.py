from apps.catalog.models import OrgDirection
from apps.images.models import Image
from django import forms
from django.contrib import admin
from django.utils.html import mark_safe

from .models import Organisation


class OrgPhotoInline(admin.TabularInline):
    model = Image
    extra = 0
    max_num = 8
    readonly_fields = ("image_preview",)
    exclude = ("doctor", "user")
    verbose_name = "Photo"
    verbose_name_plural = "Photos"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(org__isnull=False, content_type="org_photo")

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            kwargs["choices"] = [("org_photo", "Organisation Photo")]
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


class OrgLogoInline(admin.TabularInline):
    model = Image
    extra = 0
    max_num = 1
    readonly_fields = ("image_preview",)
    exclude = ("doctor", "user")
    verbose_name = "Logo"
    verbose_name_plural = "Logo"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(org__isnull=False, content_type="org_logo")

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            kwargs["choices"] = [("org_logo", "Organisation Logo")]
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


class OrganisationAdminForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = "__all__"

    org_directions = forms.ModelMultipleChoiceField(
        queryset=OrgDirection.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "checkbox-multiple-columns"}
        ),
    )

    class Media:
        css = {"all": ("organisations/admin_custom.css",)}


class OrganisationAdmin(admin.ModelAdmin):
    form = OrganisationAdminForm
    exclude = ("org_slug", "org_photos", "org_rating")
    list_display = (
        "org_id",
        "org_name",
        "org_slug",
        "org_category_display",
        "is_active",
        "updated_at",
    )
    search_fields = ["org_name"]
    list_filter = ["org_category", "is_active"]

    inlines = [OrgPhotoInline, OrgLogoInline]

    def org_category_display(self, obj):
        return obj.org_category.name if obj.org_category else None

    org_category_display.short_description = "Org Category"


admin.site.register(Organisation, OrganisationAdmin)
