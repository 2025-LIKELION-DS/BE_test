from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField()
    # username=models.CharField(unique=True)

    def __str__(self):
        return self.username
