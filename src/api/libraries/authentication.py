from src.constants import *
from src.models.user import User
from src.models.token import Token
from rest_framework import exceptions
from rest_framework import authentication

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        user_token   = request.META.get(USER_TOKEN, False)
        if user_token:
            try:
                token = Token.objects.get_access_token(access_token=user_token)
            except Exception as e:
                raise exceptions.AuthenticationFailed('Invalid access token')
            user_id = token.user
            user = User.objects.get(user_id=user_id)
            return (user, token)
        else:
            return None

    def authenticate_header(self, request):
        return ['token']