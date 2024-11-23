from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views import View

from config.api import api


class google_callback_view(View):
    pass


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Auth
    path("auth/", include("allauth.headless.urls")),
    # API
    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
