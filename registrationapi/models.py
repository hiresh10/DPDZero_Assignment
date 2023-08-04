from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

