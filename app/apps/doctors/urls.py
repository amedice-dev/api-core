from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DoctorsViewSet
from apps.organisations.urls import NoTrailingSlashRouter


router = NoTrailingSlashRouter()
router.register(r"doctors", DoctorsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
