from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination

from .models import Organisation
from .schema_parameters import (
    ID_PARAMETER,
    ORG_CATEGORY_PARAMETER,
    ORG_DIRECTION_PARAMETER,
    PAGE_PARAMETER,
    PAGE_SIZE_PARAMETER,
)
from .serializers import (
    OrganisationsSerializer,
    OrganisationPostSerializer,
    OrganisationDetailSerializer,
)
from users.permissions import IsOwner, IsOrgAdmin, CanUpdateOrganisation


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = (
        "page_size"  # The name of the request parameter for specifying the page size
    )
    max_page_size = 100  # Maximum page size


class OrganisationsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Organisation.objects.all()
    serializer_class = OrganisationsSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    pagination_class = CustomPageNumberPagination

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            permission_classes = [IsOwner]  # Only Owner can create Organisation
        elif self.action in ["update", "partial_update"]:
            permission_classes = [
                (IsOwner | IsOrgAdmin) & CanUpdateOrganisation
            ]  # Only Owner or OrgAdmin can update and delete Organisation
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        # Use different serializer for different actions
        if self.action == "create":
            return OrganisationPostSerializer
        if self.action == "list":
            return OrganisationsSerializer
        if self.action == "retrieve":
            return OrganisationDetailSerializer
        if self.action == "update" or self.action == "partial_update":
            return OrganisationDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        # Set org_owner before saving Organisation
        serializer.validated_data["org_owner"] = self.request.user
        serializer.save()

        # Add the new organisation's ID to the current user's organisations_list
        org_id = serializer.instance.org_id
        self.request.user.organisations_list.add(org_id)
        self.request.user.save()

    @extend_schema(
        parameters=[
            ORG_CATEGORY_PARAMETER,
            ORG_DIRECTION_PARAMETER,
            PAGE_PARAMETER,
            PAGE_SIZE_PARAMETER,
        ]
    )
    def list(self, request, *args, **kwargs):
        """Получение списка организаций с фильтрацией и пагинацией."""
        org_category = request.query_params.get("org_category", None)
        org_direction = request.query_params.get("org_direction", None)

        queryset = Organisation.objects.filter(is_active=True)

        if org_category:
            if not Organisation.objects.filter(
                org_category__slug=org_category
            ).exists():
                raise NotFound(detail="Организация с указанной категорией не найдена")
            queryset = queryset.filter(org_category__slug=org_category)

        if org_direction:
            if not Organisation.objects.filter(
                org_directions__slug=org_direction
            ).exists():
                raise NotFound(detail="Организация с указанным направлением не найдена")
            queryset = queryset.filter(org_directions__slug=org_direction)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OrganisationsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OrganisationsSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=OrganisationPostSerializer,
        responses={status.HTTP_201_CREATED: OrganisationsSerializer()},
    )
    def create(self, request, *args, **kwargs):
        """Создание новой организации."""
        return super().create(request, *args, **kwargs)

    @extend_schema(
        parameters=[
            ID_PARAMETER,
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        """Получение полной информации об одной организации."""
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        parameters=[
            ID_PARAMETER,
        ]
    )
    def partial_update(self, request, *args, **kwargs):
        """Обновление данных организации."""
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        parameters=[
            ID_PARAMETER,
        ]
    )
    def destroy(self, request, *args, **kwargs):
        """Удаление организации."""
        return super().destroy(request, *args, **kwargs)
