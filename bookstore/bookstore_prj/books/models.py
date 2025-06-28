from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="books")
    plot=models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    book=models.ForeignKey(to=Book,on_delete=models.CASCADE,related_name='reviews')
    writer=models.CharField(max_length=20)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"[{self.writer}] {self.book}"