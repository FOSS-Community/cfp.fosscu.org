from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self,firstname,lastname,email,password,**extra):
        if not email:
            raise ValueError('You have not provided a valid email')
        
        email=self.normalize_email(email)
        if not firstname and not extra['is_superuser']:
            raise ValueError('You must have a first name')
        if not lastname and not extra['is_superuser']:
            raise ValueError('You must have a last name')
        
        user=self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,firstname=None,lastname=None,email=None,password=None,**extra):
        extra.setdefault('is_staff',False)
        extra.setdefault('is_superuser',False)
        extra.setdefault('is_active',True)
        return self._create_user(firstname,lastname,email,password,**extra)
    
    def create_superuser(self,firstname='admin',lastname='',email=None,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return self._create_user(firstname,lastname,email,password,**extra)


class UserModel(AbstractBaseUser,PermissionsMixin):
    firstname=models.CharField(max_length=100,default='')
    lastname=models.CharField(max_length=100,default='')
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
    



    