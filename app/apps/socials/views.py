from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import OrgSocials
from .serializers import OrgSocialsSerializer


class SocialsViewSet(viewsets.ModelViewSet):
    queryset = OrgSocials.objects.all()
    serializer_class = OrgSocialsSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
