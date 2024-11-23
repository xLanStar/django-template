from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.utils.translation import gettext as _


class UserManager(DjangoUserManager):
    """Custom manager for the User model."""

    def _create_user(self, name: str, email: str, password: str, **extra_fields: dict) -> AbstractBaseUser:
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError(_("The given email must be set"))

        user = self.model(
            name=self.model.normalize_username(name),
            email=self.normalize_email(email),
            password=make_password(password),
            **extra_fields,
        )
        user.save(using=self._db)
        return user

    def create_user(self, name: str, email: str, password: str, **extra_fields: dict) -> AbstractBaseUser:
        """Create and save a regular user with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name: str, email: str, password: str, **extra_fields: dict) -> AbstractBaseUser:
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(name, email, password, **extra_fields)
