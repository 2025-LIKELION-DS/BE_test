from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required


def main(request):
    books = Book.objects.all().order_by('-id')
    
    return render(request, 'books/main.html', {'books': books})


@login_required
def detail(request,id):
    book=get_object_or_404(Book,id=id)
    return render(request,'books/detail.html',{'book':book})

@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        content = request.POST.get("content")
        created_at=request.POST.get('created_at')

        Review.objects.create(
            book=book,
            content=content,
            writer=request.user.username,  
            created_at=created_at
        )
        return redirect("books:detail", id=book_id)