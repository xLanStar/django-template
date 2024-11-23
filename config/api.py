from django.utils.translation import gettext as _
from ninja import NinjaAPI, Redoc

from features.core.api import router as user_router

api = NinjaAPI(docs=Redoc())

api.add_router("user", user_router, tags=[_("User")])
