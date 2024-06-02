from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=30)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    def __str__(self):
        return f"Name:{ self.first_name, self.last_name } Email:{ self.email}"