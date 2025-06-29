from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    books=Book.objects.all().order_by('-id')
    return render(request,'books/main.html',{'books':books})

def detail(reqeust,id):
    book=get_object_or_404(Book,id=id)
    reviews=book.book_review.all()
    return render(reqeust,'books/detail.html',{'book':book,'reviews':reviews})


@login_required
def create_review(request, book_id):
    book=get_object_or_404(Book,id=book_id)
    if request.method=="POST":
        
        content=request.POST.get('content')
        created_at=request.POST.get('created_at')

        Review.objects.create(
            book=book,
            content=content,
            writer=request.user,
            created_at=created_at,
        )
        return redirect('books:detail',book_id)