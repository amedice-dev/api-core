from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from users.views import UserRegistrationAPIView

urlpatterns = [
    # organisations
    path("", include("organisations.urls")),
    # doctors
    path("", include("doctors.urls")),
    # admin panel
    path("admin/", admin.site.urls),
    # users
    # authentication
    path("auth/register/", UserRegistrationAPIView.as_view(), name="register_user"),
    path(
        "auth/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "auth/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # swagger
    path("", include("spectacular.urls")),
]
