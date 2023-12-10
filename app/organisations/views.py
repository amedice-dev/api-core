from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .models import Organisation
from .serializers import OrganisationsSerializer, OrganisationPostSerializer
from users.permissions import IsOwner, IsOrgAdmin, IsVisitor, CanUpdateOrganisation


class OrganisationsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Organisation.objects.all()
    serializer_class = OrganisationsSerializer
    http_method_names = ["get", "post", "patch", "delete"]

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
        return super().get_serializer_class()

    def perform_create(self, serializer):
        # Set org_owner before saving Organisation
        serializer.validated_data["org_owner"] = self.request.user
        serializer.save()

        # Add the new organisation's ID to the current user's organisations_list
        org_id = serializer.instance.org_id
        self.request.user.organisations_list.add(org_id)
        self.request.user.save()

    @swagger_auto_schema(
        request_body=OrganisationPostSerializer,
        responses={status.HTTP_201_CREATED: OrganisationsSerializer()},
    )
    def create(self, request, *args, **kwargs):
        """Создание организации"""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return Response(status=405)
