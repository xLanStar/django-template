from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField

from common.models import BaseModel
from features.core.managers import UserManager
from utils.storage import get_file_upload_path


class User(AbstractUser, BaseModel):
    """User model."""

    name = CharField(
        _("username"),
        max_length=254,
        blank=True,
    )
    email = EmailField(
        _("email address"),
        unique=True,
    )
    password = CharField(
        _("password"),
        max_length=128,
        blank=True,
    )
    avatar = ImageField(
        upload_to=get_file_upload_path,
        verbose_name=_("avatar"),
        blank=True,
        null=True,
    )
    time_zone = TimeZoneField(
        _("time zone"),
        default="UTC",
    )

    first_name = None
    last_name = None
    username = None
    date_joined = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = []

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering: ClassVar[list[str]] = ["-created_at"]
