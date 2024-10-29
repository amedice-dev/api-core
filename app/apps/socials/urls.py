from apps.organisations.urls import NoTrailingSlashRouter
from django.urls import include, path

from .views import SocialsViewSet

router = NoTrailingSlashRouter()
router.register(r"socials", SocialsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("socials", SocialsListCreateAPIView.as_view(), name="socials_list"),
    # path("socials/<int:org_id>", SocialsRetrieveUpdateDestroyAPIView.as_view(), name="socials_methods"),
    # path("socials/<int:org_id>/delete", SocialsDeleteAPIView.as_view(), name="socials_delete"),
]
