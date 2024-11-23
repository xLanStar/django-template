from allauth.socialaccount.signals import (
    social_account_added,
    social_account_removed,
    social_account_updated,
    pre_social_login,
)
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    print("user_signed_up", request, user)


# 新增第三方帳號，首次登入的第三方帳號不會觸發
@receiver(social_account_added)
def social_account_added_handler(request, sociallogin, **kwargs):
    print("social_account_added", request, sociallogin)


@receiver(social_account_removed)
def social_account_removed_handler(request, socialaccount, **kwargs):
    print("social_account_removed", request, socialaccount)


@receiver(social_account_updated)
def social_account_updated_handler(request, sociallogin, **kwargs):
    print("social_account_updated", request, sociallogin)
    print(sociallogin.user)
    print(sociallogin.account)


@receiver(pre_social_login)
def pre_social_login_handler(request, sociallogin, **kwargs):
    print("pre_social_login", request, sociallogin)
    print(sociallogin.user)
    print(sociallogin.email_addresses)
