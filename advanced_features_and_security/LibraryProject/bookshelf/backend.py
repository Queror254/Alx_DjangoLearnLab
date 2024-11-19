from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.conf import settings
from .models import CustomUser

class EmailAuthBackend(BaseBackend):
    """
    Authenticate users using their email and password.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
