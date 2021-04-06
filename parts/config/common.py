"""
Django settings for parts project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import datetime
import os

from configurations import Configuration
from os.path import join
from pathlib import Path
from manage import get_secret


class Common(Configuration):

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret("SECRET_KEY")
    DATABASES = {"default": get_secret("secret_DB")}
    LOGIN_URL = "/api/v1/auth/login/"
    ALLOWED_HOSTS = ["*"]
    ASGI_APPLICATION = "parts.routing.application"
    WSGI_APPLICATION = "parts.wsgi.application"
    LOGIN_REDIRECT_URL = "/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    AUTH_USER_MODEL = "core.AuthUser"
    # SECURITY WARNING: don't run with debug turned on in production!

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "corsheaders",
        "parts.core",
        "parts.requests",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "parts.middleware.AuthenticationMiddlewareJWT",
    ]

    ROOT_URLCONF = "parts.urls"

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

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "parts.core.pagination.CustomPagination",
        "PAGE_SIZE": 10,
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_PERMISSION_CLASSES": [
            # 'rest_framework.permissions.IsAuthenticated',
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
            # "rest_framework.authentication.BasicAuthentication",
        ),
        "DEFAULT_FILTER_BACKENDS": (
            "django_filters.rest_framework.DjangoFilterBackend",
        ),
        "DEFAULT_THROTTLE_CLASSES": [
            "rest_framework.throttling.ScopedRateThrottle",
            "rest_framework.throttling.AnonRateThrottle",
        ],
        "DEFAULT_THROTTLE_RATES": {"anon": "5000/day", "user_throttle": "5000/day"},
    }

    JWT_AUTH = {
        "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
        "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
        "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
        # 'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        #   'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
        "JWT_RESPONSE_PAYLOAD_HANDLER": "parts.core.jwt_overrides.jwt_response_payload_handler",
        # "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_response_payload_handler",
        "JWT_SECRET_KEY": SECRET_KEY,
        "JWT_PUBLIC_KEY": None,
        "JWT_PRIVATE_KEY": None,
        "JWT_ALGORITHM": "HS256",
        "JWT_VERIFY": True,
        "JWT_VERIFY_EXPIRATION": True,
        "JWT_LEEWAY": 0,
        "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=1),
        "JWT_AUDIENCE": None,
        "JWT_ISSUER": None,
        "JWT_ALLOW_REFRESH": True,
        "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
        # 'JWT_AUTH_HEADER_PREFIX': 'JWT',
        "JWT_AUTH_COOKIE": "jwt",
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    STATIC_ROOT = join(os.path.dirname(BASE_DIR), "static")
    STATIC_URL = "/static/"
    STATICFILES_DIRS = ["parts/static/templates"]
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), "media")
    MEDIA_URL = "/media/"
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": STATICFILES_DIRS,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]