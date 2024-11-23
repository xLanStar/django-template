from typing import ClassVar

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from features.core.forms import UserAdminChangeForm, UserAdminCreationForm
from features.core.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """User admin."""

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (
            _("Basic"),
            {
                "fields": (
                    "email",
                    "password",
                    "name",
                    "avatar",
                    "time_zone",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    list_display: ClassVar[list[str]] = [
        "id",
        "email",
        "name",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "created_at",
    ]
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering: ClassVar[list[str]] = ["-created_at"]
