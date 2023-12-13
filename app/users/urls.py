from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet
from organisations.urls import NoTrailingSlashRouter

router = NoTrailingSlashRouter()

router.register(r"users", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
