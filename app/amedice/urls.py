from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from apps.users.views import UserRegistrationAPIView


api_urlpatterns = [
    # catalog of categories and directions
    path("catalog/", include("apps.catalog.urls")),

    # organisations
    path("", include("apps.organisations.urls")),

    # social media
    path("", include("apps.socials.urls")),

    # doctors
    path("", include("apps.doctors.urls")),

    # users (temporary)
    path("", include("apps.users.urls")),

    # images
    path("images/", include("apps.images.urls")),

    # authentication
    path("auth/register", UserRegistrationAPIView.as_view(), name="register_user"),
    path("auth/login", jwt_views.TokenObtainPairView.as_view(), name="login_user"),
    path(
        "auth/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("auth/logout", jwt_views.TokenBlacklistView.as_view(), name="logout_user"),

    # swagger
    path("", include("spectacular.urls")),
]

urlpatterns = [
    path("api/", include(api_urlpatterns)),
    # admin panel
    path("api/admin/", admin.site.urls),
    # debug toolbar
    # path("api/__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
