from apps.users.views import UserRegistrationAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from .config import get_settings

config = get_settings()
debug = config.application.debug

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
]

if debug:
    # swagger
    api_urlpatterns += [
        path("", include("spectacular.urls")),
    ]

debug_urlpatterns = [
    # debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns = [
    path("api/", include(api_urlpatterns)),
    # admin panel
    path("control-panel/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if debug:
    urlpatterns += debug_urlpatterns
