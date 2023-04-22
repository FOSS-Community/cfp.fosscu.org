from django.db import models
from  users.models import Profile

# Create your models here.
class talks(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=400)
    domain=models.CharField(max_length=50)
    slides=models.BooleanField(verbose_name="Yes",default=False)
    firstname=models.ForeignKey(Profile,on_delete=models.CASCADE)
    duration=models.DurationField()
    availability=models.DateField()

    def __str__(self):
        return self.title