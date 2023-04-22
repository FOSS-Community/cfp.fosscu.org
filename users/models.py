from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
from django.utils import timezone
# Create your models here.

class CustomUserManager(UserManager):

    def _create_user(self,first_name,last_name,email,password,**extra):
        if not email:
            raise ValueError('You have not provided a valid email')
        
        email=self.normalize_email(email)
        if not first_name:
            raise ValueError('You must have a first name')
        if not last_name:
            raise ValueError('You must have a last name')
        
        user=self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return _create_user(self,first_name,last_name,email,password,**extra):
    
    def create_user(self,first_name=None,last_name=None,email=None,password=None,**extra):
        extra.setdefault('is_staff',False)
        extra.setdefault('is_superuser',False)
        extra.setdefault('is_active',True)
        return     
    def create_superuser(self,first_name=None,last_name=None,email=None,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return _create_user(self,first_name,last_name,email,password,**extra)


class UserModel(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=100,blank=False,default='')
    last_name=models.CharField(max_length=100,blank=False,default='')
    email=models.EmailField(blank=False,unique=True,default='')
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(blank=True,null=True)

    objects=CustomUserManager()
    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta():
        verbose_name='UserModel'
        verbose_name_plural='UserModel'

    def get_full_name(self):
        return self.first_name + self.last_name








class Profile(models.Model):
    first_name=models.CharField(max_length=100,null=False,default='')
    last_name=models.CharField(max_length=100,null=False,default='')
    email=models.EmailField(null=False,unique=True)
    mobile=models.BigIntegerField()
    about=models.TextField(max_length=400)
    verified=models.BooleanField(verbose_name='verified',default=False)

    def __str__(self):
        return self.username
    



    