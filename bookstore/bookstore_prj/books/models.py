from django.db import models
from accounts.models import *

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    plot=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    book=models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='book')
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user')
    content=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.writer.username} - {self.book.title}"