from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend:
    '''Custom Authentication Backend
        Allow users to authenticate using email'''
    
    def authenticate(self,response,username=None,password=None,**extra_fields):
        
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            return "phli condition false"
        except UserModel.DoesNotExist:
            return "dusri condition false"
        
    
    def get_user(self,user_id):
        UserModel=get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return "teesri condition false"
    