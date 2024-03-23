from django.contrib import admin

from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):

    readonly_fields = ('org_slug',)
    list_display = ('org_id', 'org_name', 'org_slug', 'org_category_display', 'is_active', 'updated_at')
    search_fields = ['org_name']
    list_filter = ['org_category', 'is_active']

    def org_category_display(self, obj):
        return obj.org_category.name if obj.org_category else None

    org_category_display.short_description = 'Org Category'


admin.site.register(Organisation, OrganisationAdmin)
