from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class EmailAuthBackend(BaseBackend):
    def authenticate(self, response, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        else:
            return None

    
    def get_user(self,user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
    