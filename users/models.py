from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
from .managers import CustomUserManager


# Create your models here.


class UserModel(AbstractUser,PermissionsMixin):
    first_name=models.CharField(max_length=100,null=False,default='')
    last_name=models.CharField(max_length=100,null=False,default='')
    username=None
    email=models.EmailField(unique=True,default='',null=False,blank=False)
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
        return self.firstname + self.lastname




class Profile(models.Model):
    firstname=models.CharField(max_length=100,null=False,default='')
    lastname=models.CharField(max_length=100,null=False,default='')
    email=models.EmailField(null=False,unique=True)
    mobile=models.BigIntegerField()
    about=models.TextField(max_length=400)
    verified=models.BooleanField(verbose_name='verified',default=False)

    def __str__(self):
        return self.username
    