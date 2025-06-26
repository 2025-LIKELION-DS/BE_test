from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    plot=models.TextField()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book=models.ForeignKey(to=Book,on_delete=models.CASCADE,related_name='book_review')
    writer=models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE, related_name='review_writer')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.writer}-{self.book}