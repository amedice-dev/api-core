from django.urls import include, path
from rest_framework.routers import DefaultRouter

from organisations.urls import NoTrailingSlashRouter
from .views import (
    SocialsViewSet,
)


router = NoTrailingSlashRouter()
router.register(r"socials", SocialsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]