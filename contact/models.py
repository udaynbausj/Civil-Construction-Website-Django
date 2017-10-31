from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class userprofile(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField()
    description = models.TextField()

class subscribe_model(models.Model):
    Email = models.EmailField()



