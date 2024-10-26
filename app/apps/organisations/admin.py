from django import forms
from django.contrib import admin

from .models import Organisation
from apps.images.models import OrgPhoto, OrgLogo


class OrgPhotoInline(admin.TabularInline):
    model = OrgPhoto
    extra = 1
    max_num = 8


class OrgLogoInline(admin.TabularInline):
    model = OrgLogo
    extra = 1


class OrganisationAdminForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationAdmin(admin.ModelAdmin):
    form = OrganisationAdminForm
    exclude = ('org_slug', 'org_photos', 'org_rating')
    list_display = ('org_id', 'org_name', 'org_slug', 'org_category_display', 'is_active', 'updated_at')
    search_fields = ['org_name']
    list_filter = ['org_category', 'is_active']
    inlines = [OrgPhotoInline, OrgLogoInline]

    def org_category_display(self, obj):
        return obj.org_category.name if obj.org_category else None

    org_category_display.short_description = 'Org Category'


admin.site.register(Organisation, OrganisationAdmin)

