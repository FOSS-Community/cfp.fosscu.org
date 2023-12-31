from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser

from .models import UserModel

from typing import Optional


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email, password, **kwargs) -> Optional[AbstractUser]:
        UserModel = get_user_model()
        try:
            user: AbstractUser = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
                return user
        return None
    
    def get_user(self, user_id) -> Optional[AbstractUser]:
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
