from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount, SocialLogin
from allauth.socialaccount.signals import (
    pre_social_login,
    social_account_added,
    social_account_removed,
    social_account_updated,
)
from django.dispatch import receiver
from django.http import HttpRequest

from features.core.models import User


@receiver(user_signed_up)
def user_signed_up_handler(request: HttpRequest, user: User, **kwargs: dict) -> None:
    """Handler for user_signed_up signal."""


@receiver(social_account_added)
def social_account_added_handler(request: HttpRequest, sociallogin: SocialLogin, **kwargs: dict) -> None:
    """Handler for social_account_added signal."""


@receiver(social_account_removed)
def social_account_removed_handler(request: HttpRequest, socialaccount: SocialAccount, **kwargs: dict) -> None:
    """Handler for social_account_removed signal."""


@receiver(social_account_updated)
def social_account_updated_handler(request: HttpRequest, sociallogin: SocialLogin, **kwargs: dict) -> None:
    """Handler for social_account_updated signal."""


@receiver(pre_social_login)
def pre_social_login_handler(request: HttpRequest, sociallogin: SocialLogin, **kwargs: dict) -> None:
    """Handler for pre_social_login signal."""
