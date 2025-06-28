from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.


def main(request):
    books = Book.objects.all().order_by('-id') #id 역순으로 가져오겠다는 뜻. 디비 (최신글부터 볼 수 있음)
    return render(request, 'books/main.html', {'books':books})


def detail(request,id):
    book = get_object_or_404(Book , id=id)
    return render(request, 'books/detail.html', {'book':book})

def create_review(request, post_id):
    book = get_object_or_404(Book , id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        writer=request.user.username

        Review.objects.create(
            book=book,
            content=content,
            writer=writer
        )
        return redirect('books:detail', post_id)
    return redirect('books:main')