from apps.organisations.urls import NoTrailingSlashRouter
from django.urls import include, path

from .views import DoctorsViewSet

router = NoTrailingSlashRouter()
router.register(r"doctors", DoctorsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
