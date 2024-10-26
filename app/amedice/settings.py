import os
import dj_database_url
from datetime import timedelta
from pathlib import Path

from django.urls import reverse_lazy
from .config import get_settings

settings = get_settings()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.application.secret_key

DEBUG = settings.application.debug

ALLOWED_HOSTS = settings.application.allowed_hosts

CSRF_TRUSTED_ORIGINS = settings.application.csrf_trusted

# Application definition
INSTALLED_APPS = [
    "apps.organisations.apps.OrganisationsConfig",
    "apps.doctors.apps.DoctorsConfig",
    "apps.images.apps.ImagesConfig",
    "apps.users.apps.UsersConfig",
    "apps.reviews.apps.ReviewsConfig",
    "apps.socials.apps.SocialsConfig",
    "apps.catalog.apps.CatalogConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "debug_toolbar",
    "corsheaders",
    "rest_framework",
    "drf_yasg",
    "drf_spectacular",
    "rest_framework_simplejwt.token_blacklist",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "amedice.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "amedice.wsgi.application"


# Database
DATABASES = {
    "default": dj_database_url.config(
        default=settings.database.url, engine=settings.database.engine,
        conn_max_age=settings.database.conn_max_age, conn_health_checks=settings.database.conn_health_check
    ),
}

# Custom User model
AUTH_USER_MODEL = "users.User"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = settings.application.language

TIME_ZONE = settings.application.timezone

USE_I18N = True

USE_TZ = True

# Static
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DRF
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": settings.application.access_token_lifetime,
    "REFRESH_TOKEN_LIFETIME": settings.application.refresh_token_lifetime,
}

# DRF Spectacular Settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Amedice Aggregator API",
    "DESCRIPTION": "Документация для API агрегатора медицинских центров Amedice.",
    "VERSION": "1.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "PREPROCESSING_HOOKS": ["spectacular.hooks.remove_apis_from_list"],
    # Custom Spectacular Settings
    "EXCLUDE_PATH": [reverse_lazy("schema")],
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

# Debug Toolbar
if DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
        },
    }

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
