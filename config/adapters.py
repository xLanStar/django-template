from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email, user_username, valid_email_or_none
from allauth.headless.adapter import DefaultHeadlessAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from django.http import HttpRequest

from features.core.models import User


class HeadlessAdapter(DefaultHeadlessAdapter):
    """Custom headless adapter."""

    def serialize_user(self, user: User) -> dict:
        """Convert user to a dictionary."""
        ret = {
            "id": user.id,
            "name": user.name,
        }
        email = EmailAddress.objects.get_primary_email(user)
        if email:
            ret["email"] = email
        return ret


class AccountAdapter(DefaultAccountAdapter):
    """Custom account adapter."""


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """Custom social account adapter."""

    def populate_user(self, _: HttpRequest, sociallogin: SocialLogin, data: dict) -> User:
        """Populate user data from social account data."""
        user = sociallogin.user
        user_username(user, data.get("name") or "")
        user_email(user, valid_email_or_none(data.get("email")) or "")
        return user
