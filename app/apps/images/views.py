from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Image
from .schema_parameters import DOCTOR_ID_PARAMETER, ORG_ID_PARAMETER, USER_ID_PARAMETER
from .serializers import (
    DoctorAvatarSerializer,
    OrgLogoSerializer,
    OrgPhotoSerializer,
    UserAvatarSerializer,
)


@extend_schema(
    parameters=[
        ORG_ID_PARAMETER,
    ]
)
class OrgPhotoListAPIView(generics.ListAPIView):
    serializer_class = OrgPhotoSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        org_id = self.kwargs.get("org_id")
        try:
            queryset = Image.objects.filter(
                org_id=org_id, content_type="org_photo"
            ).order_by("order")
            if queryset.exists():
                serializer = OrgPhotoSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response(
                    {
                        "error": "Фотографий для указанного ID организации не существует."
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        except Image.DoesNotExist:
            return Response(
                {"error": "Фотографий для указанного ID организации не существует."},
                status=status.HTTP_404_NOT_FOUND,
            )


@extend_schema(
    parameters=[
        ORG_ID_PARAMETER,
    ]
)
class OrgLogoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrgLogoSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        org_id = self.kwargs.get("org_id")
        try:
            logo = Image.objects.get(org_id=org_id, content_type="org_logo")
            serializer = OrgLogoSerializer(logo)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response(
                {"error": "Логотипа для указанного ID организации не существует."},
                status=status.HTTP_404_NOT_FOUND,
            )


@extend_schema(
    parameters=[
        DOCTOR_ID_PARAMETER,
    ]
)
class DoctorAvatarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DoctorAvatarSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        doc_id = self.kwargs.get("doc_id")
        try:
            avatar = Image.objects.get(doctor_id=doc_id, content_type="doctor_avatar")
            serializer = DoctorAvatarSerializer(avatar)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response(
                {"error": "Аватара для указанного ID доктора не существует."},
                status=status.HTTP_404_NOT_FOUND,
            )


@extend_schema(
    parameters=[
        USER_ID_PARAMETER,
    ]
)
class UserAvatarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserAvatarSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get("user_id")
        try:
            avatar = Image.objects.get(user_id=user_id, content_type="user_avatar")
            serializer = UserAvatarSerializer(avatar)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response(
                {"error": "Аватара для указанного ID пользователя не существует."},
                status=status.HTTP_404_NOT_FOUND,
            )
