from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Organisation
from .serializers import OrganisationsSerializer
from users.permissions import IsOwner, IsOrgAdmin, IsVisitor


class OrganisationsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Organisation.objects.all()
    serializer_class = OrganisationsSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsOwner]  # Only Owner can create Organisation
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner | IsOrgAdmin]  # Only Owner or OrgAdmin can update and delete Organisation
        else:
            permission_classes = [IsVisitor | IsOwner | IsOrgAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # Set org_owner before saving Organisation
        serializer.validated_data['org_owner'] = self.request.user
        serializer.save()

    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsOwner, IsAuthenticated]
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.permission_classes = [IsOwner | IsOrgAdmin, IsAuthenticated]
        return super().partial_update(request, *args, **kwargs)
