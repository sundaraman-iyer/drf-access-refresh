from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique= True)
    password = models.CharField(max_length = 255)

    #setting values to none bcz, these are automatically added by django
    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
