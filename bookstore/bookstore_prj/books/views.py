from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def main(request):
    books=Book.objects.all()
    return render(request, 'books/main.html', {'books':books})

def detail(request, id):
    book=get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'books/detail.html',{'book':book, 'reviews':reviews})

@login_required
def review(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method=='POST':
        content=request.POST.get("content")
        created_at=request.POST.get("created_at")

        Review.objects.create(
            content=content,
            writer=request.user,
            created_at=created_at,
            book=book
        )
        return redirect('books:detail',id)
    return redirect('books:detail', id)