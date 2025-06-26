from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/main.html', {'books':books})

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'book':book})

@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        content = request.POST.get('content')

        Review.objects.create(
            book = book,
            writer = request.user,
            content = content
        )
        return redirect('books:detail', book_id)
    return redirect('books:main')

