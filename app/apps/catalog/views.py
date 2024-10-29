from apps.organisations.models import Organisation
from django.db.models import Count, Q
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OrgCategory, OrgDirection
from .schema_parameters import CATEGORY_SLUG_PARAMETER
from .serializers import (
    CategoryPageContentSerializer,
    OrgCategorySerializer,
    OrgCategoryWithCountSerializer,
    OrgDirectionSerializer,
)


class CategoriesAPIView(ListCreateAPIView):
    queryset = OrgCategory.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["post"]
    serializer_class = OrgCategorySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [
                IsAdminUser,
            ]
        else:
            permission_classes = [
                AllowAny,
            ]
        return [permission() for permission in permission_classes]


class DirectionsAPIView(ListCreateAPIView):
    queryset = OrgDirection.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "post"]
    serializer_class = OrgDirectionSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [
                IsAdminUser,
            ]
        else:
            permission_classes = [
                AllowAny,
            ]
        return [permission() for permission in permission_classes]


@extend_schema(responses={200: OrgCategoryWithCountSerializer(many=True)})
class CategoriesTreeView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ["get"]

    def get(self, request):
        """Получение списка категорий с количество организаций в каждой из них."""
        categories = OrgCategory.objects.annotate(
            count=Count("organisation", filter=Q(organisation__is_active=True))
        ).order_by("category_id")

        serializer = OrgCategoryWithCountSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDirectionsView(GenericAPIView):
    permission_classes = (AllowAny,)
    http_method_names = ["get"]
    serializer_class = OrgDirectionSerializer

    @extend_schema(
        parameters=[
            CATEGORY_SLUG_PARAMETER,
        ]
    )
    def get(self, request):
        """Получение списка направлений для определенной категории."""
        category_slug = request.query_params.get("category_slug")

        if not category_slug:
            return Response(
                {"error": "category_slug parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            category = OrgCategory.objects.get(slug=category_slug)
        except OrgCategory.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Get all organizations for the specified category and prefetch related OrgDirection objects
        organisations = (
            Organisation.objects.select_related("org_category")
            .prefetch_related("directions")
            .filter(org_category=category)
        )

        # Collect unique directions from these organizations
        directions = OrgDirection.objects.filter(
            organisation__in=organisations
        ).distinct()

        # Serialize and return directions
        serializer = OrgDirectionSerializer(directions, many=True)
        return Response(serializer.data)


@extend_schema(
    parameters=[CATEGORY_SLUG_PARAMETER],
    responses={200: CategoryPageContentSerializer()},
)
class CategoryPageContentView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ["get"]

    def get(self, request):
        """Получение page_content категории по slug."""
        category_slug = request.query_params.get("category_slug")

        if not category_slug:
            return Response(
                {"error": "category_slug parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            category = OrgCategory.objects.get(slug=category_slug)
        except OrgCategory.DoesNotExist:
            raise NotFound(detail="Категория с указанным slug не найдена")

        serializer = CategoryPageContentSerializer(category)
        return Response(serializer.data)
