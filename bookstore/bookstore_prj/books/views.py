from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

def main(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/main.html', {'books' :books })

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'books/detail.html', {'book':book, 'reviews':reviews})

@login_required
def create_review(request,id):

    if request.method == "POST":
        content = request.POST.get('content')
        book = get_object_or_404(Book, id=id)
        Review.objects.create(
            book = book,
            writer = request.user,
            content = content,
            )
        return redirect('books:detail',id)
    return render(request, 'books/detail.html')
