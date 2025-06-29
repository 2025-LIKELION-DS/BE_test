from django.db import models
from django.contrib.auth import get_user_model  

User = get_user_model()  

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    plot = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="BookReview")
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="ReviewWriter")  
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.writer} - {self.book}"