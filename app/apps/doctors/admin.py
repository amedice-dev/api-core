from django.contrib import admin

from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'doc_first_name', 'doc_last_name', 'doc_middle_name', 'doc_rating')


admin.site.register(Doctor, DoctorAdmin)
