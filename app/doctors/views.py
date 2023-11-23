from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Doctor
from .serializers import DoctorsSerializer


class DoctorsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
