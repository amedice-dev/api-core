from django.contrib import admin
from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    readonly_fields = ('org_slug',)  # Поле org_slug только для чтения


admin.site.register(Organisation, OrganisationAdmin)
