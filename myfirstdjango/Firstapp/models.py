from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
class Accessrecord(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class user(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=260)
    email = models.EmailField(max_length=500,unique=True)

## Userprofile
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ## additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username

