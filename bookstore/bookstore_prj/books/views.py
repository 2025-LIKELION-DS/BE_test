from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review

def main(request):
    books=Book.objects.all().order_by('-id')
    return render(request, 'books/main.html', {'books':books})

def detail(request, id):
    book=get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'book':book})

def review(request, id):
    book=get_object_or_404(Book, id=id)
    if request.method=="POST":
        text=request.POST.get('review_text')
        Review.objects.create(
            book=book,
            writer=request.user,
            content=text            
        )
        return redirect("books:detail",id)