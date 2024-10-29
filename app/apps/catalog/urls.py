from django.urls import path

from .views import (
    CategoriesAPIView,
    CategoriesTreeView,
    CategoryDirectionsView,
    CategoryPageContentView,
    DirectionsAPIView,
)

urlpatterns = [
    path("categories_tree", CategoriesTreeView.as_view()),
    path("category_directions", CategoryDirectionsView.as_view()),
    path("categories", CategoriesAPIView.as_view(), name="categories"),
    path("directions", DirectionsAPIView.as_view(), name="directions"),
    path(
        "page_content/caterory",
        CategoryPageContentView.as_view(),
        name="category_page_content",
    ),
]
