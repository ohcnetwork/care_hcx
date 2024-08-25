import jwt
import requests
from cryptography.x509 import load_pem_x509_certificate
from hcx.settings import plugin_settings as settings
from django.utils.translation import gettext_lazy as _
from drf_spectacular.extensions import OpenApiAuthenticationExtension

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from care.users.models import User

class HCXAuthentication(JWTAuthentication):
    def authenticate_header(self, request):
        return "Bearer"

    def authenticate(self, request):
        jwt_token = self.get_jwt_token(request.META.get("HTTP_AUTHORIZATION"))

        try:
            payload = self.decode_jwt(settings.HCX_CERT_URL, jwt_token)
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed("Invalid signature")
        except Exception as e:
            raise InvalidToken({"detail": str(e)})
        
        user = self.get_user()

        return user, payload

    def get_jwt_token(self, token):
        jwt_token = token.replace("Bearer ", "", 1)

        if not jwt_token:
            raise InvalidToken({"detail": "Missing Authorization token"})

        return jwt_token

    def decode_jwt(self, public_key_url, token):
        response = requests.get(public_key_url)
        cert = response.text.strip().encode()

        cert_obj = load_pem_x509_certificate(cert)
        public_key = cert_obj.public_key()

        return jwt.decode(token, key=public_key, algorithms=["RS256"])

    def get_user(self):
        user = User.objects.filter(username=settings.HCX_USERNAME).first()
        if not user:
            password = User.objects.make_random_password()
            user = User(
                username=settings.HCX_USERNAME,
                email="hcx@coronasafe.network",
                password=f"{password}123",
                gender=3,
                phone_number="917777777777",
                user_type=User.TYPE_VALUE_MAP["Volunteer"],
                verified=True,
                age=10,
            )
            user.save()
        return user


class HCXAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "authentication.HCXAuthentication"
    name = "HCXAuth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": _(
                "Used for authenticating requests from the HCX servers. "
                "The scheme requires a valid JWT token in the Authorization header."
            ),
        }