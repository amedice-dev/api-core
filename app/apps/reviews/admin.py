from django.contrib import admin

from .models import DoctorReview, OrganisationReview, Review

admin.site.register(Review)
admin.site.register(DoctorReview)
admin.site.register(OrganisationReview)
