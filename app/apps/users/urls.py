from django.urls import include, path

from .views import UsersViewSet
from apps.organisations.urls import NoTrailingSlashRouter

router = NoTrailingSlashRouter()

router.register(r"users", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
