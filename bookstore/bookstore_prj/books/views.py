from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    books = Book.objects.all()  
    return render(request, 'books/main.html', {'books': books})

def detail(request, id):
    book = get_object_or_404(Book, id=id)  
    reviews = Review.objects.filter(book=book)

    return render(request, 'books/detail.html', {'book': book, 'reviews':reviews})
@login_required
def create_review(request, book_id):
    book=get_object_or_404(Book, id=book_id)
    if request.method=='POST':
        content=request.POST.get('content')

        Review.objects.create(
            book=book,
            content=content,
            writer=request.user,
        )
        return redirect('books:detail', book_id)
    return redirect('books:main')