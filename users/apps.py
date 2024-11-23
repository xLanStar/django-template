from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    """User app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = _("Users App")

    def ready(self) -> None:
        """Import signals."""
        from users import signals  # noqa: F401
