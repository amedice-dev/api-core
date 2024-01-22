from django.db.models import Count
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema

from .api_parameters import (
    CATEGORY_SLUG_PARAMETER,
)
from organisations.models import Organisation
from .models import OrgCategory, OrgDirection
from .serializers import (
    OrgCategorySerializer,
    OrgDirectionSerializer,
)
from users.permissions import IsOwner, IsOrgAdmin, CanUpdateOrganisation


@extend_schema(responses={200: OrgCategorySerializer(many=True)})
class CategoriesTreeView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ["get"]

    def get(self, request):
        """Получение списка категорий с количество организаций в каждой из них."""
        categories = OrgCategory.objects.annotate(count=Count("organisation")).order_by(
            "category_id"
        )
        serializer = OrgCategorySerializer(categories, many=True)
        return Response(serializer.data)


@extend_schema(responses={200: OrgDirectionSerializer(many=True)})
class DirectionListView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ["get"]

    def get(self, request):
        """Получение списка направлений организаций."""
        directions = OrgDirection.objects.all()
        serializer = OrgDirectionSerializer(directions, many=True)
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
