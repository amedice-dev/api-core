from django.urls import path
from .views import OrgLogoRetrieveAPIView, DoctorAvatarRetrieveAPIView, UserAvatarRetrieveAPIView, OrgPhotoListAPIView


urlpatterns = [
    path('org_photos/<int:org_id>', OrgPhotoListAPIView.as_view(), name='org_photos'),
    path('org_logo/<int:org_id>', OrgLogoRetrieveAPIView.as_view(), name='org_logo'),
    path('user_avatar/<int:user_id>', UserAvatarRetrieveAPIView.as_view(), name='user_avatar'),
    path('doctor_avatar/<int:doc_id>', DoctorAvatarRetrieveAPIView.as_view(), name='doctor_avatar'),
]
