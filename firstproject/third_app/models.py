from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

# Create your models here.
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site=models.URLField(blank=True)

    profile_pics=models.ImageField(upload_to='profile_pics',blank=True)
    object = models.Manager()


def __str__(self):
    return  self.user.username
