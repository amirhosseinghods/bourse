from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response

from ..subserializers.user import UserSerializer
from ..subserializers.user import UserSigninSerializer

from painless.auth_token import token_expire_handler
from painless.auth_token import expires_in

class SignInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        signin_serializer = UserSigninSerializer(data = request.data)
        
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status = HTTP_400_BAD_REQUEST)

        user = authenticate(
            username = signin_serializer.data['username'],
            password = signin_serializer.data['password'] 
        )
        if not user:
            msg = _('Invalid Credentials or activate account')
            return Response({'detail': msg}, status=HTTP_404_NOT_FOUND)
            
        #TOKEN STUFF
        token, _ = Token.objects.get_or_create(user = user)
        
        #token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)     # The implementation will be described further
        user_serialized = UserSerializer(user)

        return Response({
            'user': user_serialized.data, 
            'expires_in': expires_in(token),
            'token': token.key
        }, status=HTTP_200_OK)
        