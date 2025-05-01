from django.db import models

# Create your models here.
class Guest(models.Model):
    username = models.CharField(max_length=100)
    stdnum = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.username
