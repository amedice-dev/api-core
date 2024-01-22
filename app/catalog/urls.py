from django.urls import include, path

from .views import (
    CategoriesTreeView,
    DirectionListView,
    CategoryDirectionsView,
)


urlpatterns = [
    path("categories_tree", CategoriesTreeView.as_view()),
    path("directions", DirectionListView.as_view()),
    path("category_directions", CategoryDirectionsView.as_view()),
]
