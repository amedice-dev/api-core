from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .models import OrgPhoto, OrgLogo, DoctorAvatar, UserAvatar
from .schema_parameters import ORG_ID_PARAMETER, DOCTOR_ID_PARAMETER, USER_ID_PARAMETER
from .serializers import OrgPhotoSerializer, OrgLogoSerializer, DoctorAvatarSerializer, UserAvatarSerializer


@extend_schema(
    parameters=[
        ORG_ID_PARAMETER,
    ]
)
class OrgPhotoListAPIView(generics.ListAPIView):
    serializer_class = OrgPhotoSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        org_id = self.kwargs.get('org_id')
        try:
            queryset = OrgPhoto.objects.filter(org_id=org_id)
            serializer = OrgPhotoSerializer(queryset, many=True)
            return Response(serializer.data)
        except OrgPhoto.DoesNotExist:
            return Response({"error": "Фотографий для указанного ID организации не существует."},
                            status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    parameters=[
        ORG_ID_PARAMETER,
    ]
)
class OrgLogoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrgLogoSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        org_id = self.kwargs.get('org_id')
        try:
            serializer = OrgLogoSerializer(OrgLogo.objects.get(org_id=org_id))
            return Response(serializer.data)
        except OrgLogo.DoesNotExist:
            return Response({"error": "Логотипа для указанного ID организации не существует."},
                            status=status.HTTP_404_NOT_FOUND)

@extend_schema(
    parameters=[
        DOCTOR_ID_PARAMETER,
    ]
)
class DoctorAvatarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DoctorAvatarSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        doc_id = self.kwargs.get('doc_id')
        try:
            serializer = DoctorAvatarSerializer(DoctorAvatar.objects.get(doc_id=doc_id))
            return Response(serializer.data)
        except DoctorAvatar.DoesNotExist:
            return Response({"error": "Аватара для указанного ID доктора не существует."},
                            status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    parameters=[
        USER_ID_PARAMETER,
    ]
)
class UserAvatarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserAvatarSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        try:
            serializer = UserAvatarSerializer(UserAvatar.objects.get(user_id=user_id))
            return Response(serializer.data)
        except UserAvatar.DoesNotExist:
            return Response({"error": "Аватара для указанного ID пользователя не существует."},
                            status=status.HTTP_404_NOT_FOUND)
