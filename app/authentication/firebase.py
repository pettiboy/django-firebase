from django.contrib.auth.models import User
from rest_framework import authentication
import firebase_admin.auth as auth


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        token = request.headers.get('Authorization')
        if not token:
            return None

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
            email = decoded_token["email"]
        except:
            return None

        try:
            user = User.objects.get_or_create(username=uid, email=email)
            return user
        except:
            return None
