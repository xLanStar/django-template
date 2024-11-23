from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    """User app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "features.core"
    verbose_name = _("Core App")

    def ready(self) -> None:
        """Import signals."""
        from features.core import signals  # noqa: F401
