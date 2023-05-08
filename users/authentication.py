from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model



class EmailAuthBackend(BaseBackend):
    def authenticate(self,email,password,**kwargs): #username=email
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        
            if user.check_password(password):
                return user
            
        except get_user_model().DoesNotExist:
            return None

    
    def get_user(self,user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
    