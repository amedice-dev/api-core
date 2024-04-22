# from drf_spectacular.utils import extend_schema
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import AllowAny, IsAdminUser
#
# from .models import OrgSocials
# from .schema_parameters import ORG_ID_PARAMETER
# from .serializers import OrgSocialsSerializer
# from apps.organisations.models import Organisation
#
#
# class SocialsListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = OrgSocialsSerializer
#     queryset = OrgSocials.objects.all()
#
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             permission_classes = [IsAdminUser, ]
#         else:
#             permission_classes = [AllowAny, ]
#         return [permission() for permission in permission_classes]
#
#     # def post(self, request, *args, **kwargs):
#     #     try:
#     #         org_id = request.data['org_id']
#     #         socials = OrgSocials.objects.filter(org_id=org_id)
#     #         if not socials:
#     #             self.create(request, *args, **kwargs)
#     #         else:
#     #             return Response({'error': 'Соцсети для данной Организации уже существуют.'},
#     #                             status=status.HTTP_400_BAD_REQUEST)
#     #     except Organisation.DoesNotExist:
#     #         return Response({"error": "Организация с переданным ID не найдена."},
#     #                         status=status.HTTP_404_NOT_FOUND)
#
#
# @extend_schema(
#     parameters=[
#         ORG_ID_PARAMETER,
#     ]
# )
# class SocialsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrgSocialsSerializer
#     http_method_names = ['get', 'put', 'delete']
#     org_id: int
#
#     def get_permissions(self):
#         if self.request.method in ['PUT', 'DELETE']:
#             permission_classes = [IsAdminUser]
#         else:
#             permission_classes = [AllowAny, ]
#         return [permission() for permission in permission_classes]
#
#     def retrieve(self, request, *args, **kwargs):
#         org_id = self.kwargs.get('org_id')
#         try:
#             organisation = Organisation.objects.get(org_id=org_id)
#             socials = organisation.org_socials
#             serializer = self.serializer_class(socials)
#             return Response(serializer.data)
#         except Organisation.DoesNotExist:
#             return Response({"error": "Соцсети для указанного ID организации не найдены."},
#                             status=status.HTTP_404_NOT_FOUND)
#
#     # def update(self, request, *args, **kwargs):
#     #     org_id = self.kwargs.get('org_id')
#     #     try:
#     #         socials = get_socials(org_id=org_id)
#     #         if socials:
#     #             for k, v in request.data.items():
#     #                 setattr(socials, k, v)
#     #         serializer = self.serializer_class(socials)
#     #         return Response(serializer.data)
#     #     except Organisation.DoesNotExist:
#     #         return Response({"error": "Организация с указанным ID не найдена."},
#     #                         status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, *args, **kwargs):
#         self.org_id = self.kwargs.get('org_id')
#         try:
#             return self.update(request, *args, **kwargs)
#         except Organisation.DoesNotExist:
#             return Response({"error": "Организация с указанным ID не найдена."},
#                             status=status.HTTP_404_NOT_FOUND)
#
#     # def delete(self, request, *args, **kwargs):
#     #     self.org_id = self.kwargs.get('org_id')
#     #     try:
#     #         socials = self.get_object()
#     #         if socials:
#     #             socials.delete()
#     #             return Response(status=status.HTTP_204_NO_CONTENT)
#     #         return Response({"error": "У данной организации отсутствуют Соцсети."},
#     #                         status=status.HTTP_404_NOT_FOUND)
#     #     except Organisation.DoesNotExist:
#     #         return Response({"error": "Организация с указанным ID не найдена."},
#     #                         status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, *args, **kwargs):
#         self.org_id = self.kwargs.get('org_id')
#         try:
#             return self.destroy(request, *args, **kwargs)
#         except Organisation.DoesNotExist:
#             return Response({"error": "Организация с указанным ID не найдена."},
#                             status=status.HTTP_404_NOT_FOUND)
#         except AttributeError:
#             return Response({"error": "У данной организации отсутствуют Соцсети."},
#                                     status=status.HTTP_404_NOT_FOUND)
#
#     def get_object(self):
#         organisation = Organisation.objects.get(org_id=self.org_id)
#         return organisation.org_socials
