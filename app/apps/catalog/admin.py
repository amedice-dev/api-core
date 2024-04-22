from django.contrib import admin
from .models import OrgCategory, OrgDirection


class OrgCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'slug', 'type')


class OrgDirectionAdmin(admin.ModelAdmin):
    list_display = ('direction_id', 'name', 'slug')


admin.site.register(OrgCategory, OrgCategoryAdmin)
admin.site.register(OrgDirection, OrgDirectionAdmin)
