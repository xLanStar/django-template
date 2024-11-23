from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.api import api

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Auth
    path("auth/", include("allauth.headless.urls")),
    # API
    path("api/", api.urls),
    # Media
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
