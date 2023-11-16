from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Organisation
from .serializers import OrganisationsSerializer


class OrganisationsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Organisation.objects.all().order_by("-id")
    serializer_class = OrganisationsSerializer
