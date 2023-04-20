from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False)
    mobile=models.BigIntegerField()
    about=models.TextField(max_length=400)
    verified=models.BooleanField(verbose_name='verified',default=False)

    def __str__(self):
        return self.username
    



    