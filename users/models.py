from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField, ImageField
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField

from users.managers import UserManager
from utils.common.models import BaseModel


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
    last_login = DateTimeField(
        _("last login"),
        blank=True,
        null=True,
    )
    avatar = ImageField(
        upload_to=BaseModel.get_file_path,
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
