from allauth.socialaccount.providers.google.provider import GoogleProvider


class CustomGoogleProvider(GoogleProvider):
    id = "google"
    name = "Custom Google OAuth2 Provider"

    def extract_common_fields(self, data):
        return {
            "email": data.get("email"),
            "name": data.get("name"),
            "avatar": data.get("picture"),
        }


provider_classes = [CustomGoogleProvider]
