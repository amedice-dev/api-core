from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Organisation
from .serializers import OrganisationsSerializer
from users.permissions import IsOwner, IsOrgAdmin, IsVisitor, CanUpdateOrganisation


class OrganisationsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Organisation.objects.all()
    serializer_class = OrganisationsSerializer

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

    def perform_create(self, serializer):
        # Set org_owner before saving Organisation
        serializer.validated_data["org_owner"] = self.request.user
        serializer.save()
