from django.contrib.auth.models import User

class EmailAuthBackend:
    '''Custom Authentication Backend
        Allow users to authenticate using email'''
    
    def authenticate(self,response,username=None,password=None):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
        
