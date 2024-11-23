from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from users.models import User
from users.forms import UserAdminChangeForm, UserAdminCreationForm


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
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
                )
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
                )
            },
        ),
    )
    list_display = [
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
    ordering = ["-created_at"]
