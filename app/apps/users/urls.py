from apps.organisations.urls import NoTrailingSlashRouter
from django.urls import include, path

from .views import UsersViewSet

router = NoTrailingSlashRouter()

router.register(r"users", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
