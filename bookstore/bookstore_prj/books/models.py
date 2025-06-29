from django.db import models
from django.contrib.auth.models import User

class Book (models.Model):
    title=models.CharField(max_length=20)
    author=models.TextField()
    plot=models.TextField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    writer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer_review')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)