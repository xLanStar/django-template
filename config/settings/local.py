from config.settings.base import *  # noqa
from config.settings.base import env

# General
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-yj0w5^)ntugoy4y5cbwk*iec$s03v4%32%w2jc%^ldgru71--r",
)

# https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=[".localhost", "127.0.0.1", "[::1]", "localhost:8081"],
)

# Django Query Inspector
# ------------------------------------------------------------------------------

QUERY_INSPECT_ENABLED = env.bool("QUERY_INSPECT_ENABLED", default=True)


# Application definition
# ------------------------------------------------------------------------------

if QUERY_INSPECT_ENABLED:
    INSTALLED_APPS += [  # noqa
        "query_inspector",
    ]


# Middleware
# ------------------------------------------------------------------------------

if QUERY_INSPECT_ENABLED:
    MIDDLEWARE += [  # noqa
        "query_inspector.middleware.QueryCountMiddleware",
    ]

# CORS
# ------------------------------------------------------------------------------
# https://github.com/adamchainz/django-cors-headers?tab=readme-ov-file#cors_allowed_origins-sequencestr
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=[
        "http://localhost:8081",
    ],
)


# Cache
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/5.1/topics/cache/#setting-up-the-cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://127.0.0.1:6379/0"),
    },
}
