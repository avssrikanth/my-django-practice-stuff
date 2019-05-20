from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
    first_name=models.CharField(max_length=264,unique=True)
    last_name=models.CharField(max_length=264,unique=True)
    email=models.EmailField()
    object = models.Manager()



    

