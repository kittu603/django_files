from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    #create an instance to grab all inbuilt attributes from User model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional attributes

    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.first_name

