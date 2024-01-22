from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OrganisationsViewSet,
    CategoriesTreeView,
    DirectionListView,
    CategoryDirectionsView,
)


class NoTrailingSlashRouter(DefaultRouter):
    """Use this router to remove trailing slash from URLs"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register(r"organisations", OrganisationsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categories_tree", CategoriesTreeView.as_view(), name="categories_tree"),
    path("directions", DirectionListView.as_view(), name="directions"),
    path("category_directions", CategoryDirectionsView.as_view(), name="category_directions"),
]
