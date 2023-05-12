
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    

    def _create_user(self,first_name,last_name,email,password,**extra):
        if not email:
            raise ValueError('You have not provided a valid email')
        email=self.normalize_email(email)

        if not first_name and not extra['is_superuser']:
            raise ValueError('You must have a first name')
        
        if not last_name and not extra['is_superuser']:
            raise ValueError('You must have a last name')
        
        user=self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,first_name='admin',last_name='',email=None,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return self._create_user(first_name,last_name,email,password,**extra)
