from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# https://www.uvicorn.org/#quickstart
ASGI_APPLICATION = "config.asgi.application"

# https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Internationalization
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/5.1/topics/i18n/
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "zh-Hant"

# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "Asia/Taipei"

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = (
    ("en", _("English")),
    ("ja", _("Japanese")),
    ("zh-hant", _("Traditional Chinese")),
)


# Application definition
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    # "django.contrib.sessions", We are not using database-backed sessions
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # 'allauth.socialaccount.providers.apple',
    "allauth.socialaccount.providers.google",
    "corsheaders",
    "storages",
]

LOCAL_APPS = [
    "features.core",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]


# Router
# ------------------------------------------------------------------------------

# https://django-storages.readthedocs.io/en/latest/#installation
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/4.0/ref/settings/#append-slash
APPEND_SLASH = True


# Database
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
        "ATOMIC_REQUESTS": True,
    },
}

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS
# ------------------------------------------------------------------------------

# https://github.com/adamchainz/django-cors-headers?tab=readme-ov-file#cors_allowed_origins-sequencestr
CORS_ALLOWED_ORIGINS = []

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

# Session
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-age
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-name
SESSION_COOKIE_NAME = "sessionid"

# https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# https://docs.djangoproject.com/en/5.1/topics/cache/#setting-up-the-cache
CACHES = {}


# AUTHENTICATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-user-model
AUTH_USER_MODEL = "core.User"

# https://docs.allauth.org/en/dev/account/configuration.html#configuration
ACCOUNT_USER_MODEL_USERNAME_FIELD = "name"

# https://docs.allauth.org/en/dev/account/configuration.html#configuration
ACCOUNT_EMAIL_REQUIRED = True

# https://docs.allauth.org/en/dev/account/configuration.html#configuration
ACCOUNT_USERNAME_REQUIRED = True

# https://docs.allauth.org/en/dev/account/configuration.html#configuration
ACCOUNT_AUTHENTICATION_METHOD = "email"

# https://docs.allauth.org/en/dev/account/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

LOGIN_REDIRECT_URL = "admin/"

# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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

ACCOUNT_ADAPTER = "config.adapters.AccountAdapter"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
            "openid",
            "https://www.googleapis.com/auth/calendar",
        ],
        "AUTH_PARAMS": {
            "access_type": "offline",
        },
        "OAUTH_PKCE_ENABLED": False,
        "FETCH_USERINFO": True,
    },
}

SOCIALACCOUNT_STORE_TOKENS = True

SOCIALACCOUNT_ADAPTER = "config.adapters.SocialAccountAdapter"

HEADLESS_ONLY = True

HEADLESS_ADAPTER = "config.adapters.HeadlessAdapter"


# Pagination
# ------------------------------------------------------------------------------

NINJA_PAGINATION_CLASS = "ninja.pagination.LimitOffsetPagination"

NINJA_PAGINATION_PER_PAGE = 20


# Storages
# ------------------------------------------------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

ALLOW_S3 = env("ALLOW_S3", default=False)

if ALLOW_S3:
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default=None)

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

# Static files (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = "static/"

if ALLOW_S3 and env("STATIC_STORAGE_USE_S3", default=False):
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    STORAGES["staticfiles"]["BACKEND"] = "utils.storage.StaticS3Storage"

    # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = f"https://{aws_s3_domain}/static/"
else:
    # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = BASE_DIR / "static"

    # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = "static/"


# Media files
# ------------------------------------------------------------------------------


if ALLOW_S3 and env("MEDIA_STORAGE_USE_S3", default=False):
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    STORAGES["default"]["BACKEND"] = "utils.storage.MediaS3Storage"

    # https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = f"https://{aws_s3_domain}/media/"
else:
    # https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = BASE_DIR / "media"

    # https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = "media/"


# TEMPLATES
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": ["templates"],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"


# Mail
# ------------------------------------------------------------------------------

EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default=None)
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default=None)


# Default primary key field type
# -------------------------------------------------------------------------

# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
