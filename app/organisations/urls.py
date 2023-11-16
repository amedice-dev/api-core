from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrganisationsViewSet

router = DefaultRouter()

router.register(r"organisations", OrganisationsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
