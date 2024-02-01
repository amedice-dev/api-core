from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.permissions import IsOwner, IsOrgAdmin

from .models import OrgSocials
from .serializers import OrgSocialsSerializers


class SocialsViewSet(viewsets.ModelViewSet):
    queryset = OrgSocials.objects.all()
    serializer_class = OrgSocialsSerializers
    http_method_names = ["get", "post", "patch", "delete"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsOwner]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
