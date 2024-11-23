from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.headless.adapter import DefaultHeadlessAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from allauth.account.utils import user_username, user_email, valid_email_or_none

from users.models import User


class HeadlessAdapter(DefaultHeadlessAdapter):
    def serialize_user(self, user: User):
        ret = {
            "id": user.pk,
            "name": user.name,
        }
        email = EmailAddress.objects.get_primary_email(user)
        if email:
            ret["email"] = email
        return ret


class AccountAdapter(DefaultAccountAdapter):
    def new_user(self, request):
        print("AccountAdapter.new_user", request)
        return super().new_user(request)
    def save_user(self, request, user, form, commit=True):
        print("AccountAdapter.save_user", request, user, form, commit)
        return super().save_user(request, user, form, commit)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin: SocialLogin, form=None):
        print("SocialAccountAdapter.save_user", request, sociallogin, form)
        print(sociallogin.token)
        return super().save_user(request, sociallogin, form)

    def populate_user(self, request, sociallogin, data):
        print("SocialAccountAdapter.populate_user", request, sociallogin, data)
        user = sociallogin.user
        user_username(user, data.get("name") or "")
        user_email(user, valid_email_or_none(data.get("email")) or "")
        return user
