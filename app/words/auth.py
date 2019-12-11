from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model


class CustomAuthentication(TokenAuthentication):
    keyword = 'Secret'
    def authenticate_credentials(self, key):
        User = get_user_model()
        if key == settings.CUSTOM_TOKEN:
            user = User.objects.get(pk=1)
            return (user, key)
        else:
            raise exceptions.PermissionDenied('Invalid token.', code=403)
