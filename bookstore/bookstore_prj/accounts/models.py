from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    plot = models.TextField()
    
    def __str__(self):
        return self.title
    

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.username
    
class Review(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="reviews")
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.writer}] self.book'


    

