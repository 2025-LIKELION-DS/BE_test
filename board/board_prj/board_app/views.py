from django.shortcuts import render,redirect
from .forms import GuestForm
from .models import Guest

def board(request):
    
    if request.method=='POST':
        board=GuestForm(request.POST)
        if board.is_valid():
            board.save()
            return redirect('board_app:board')
    
    else:
        board=GuestForm()
    
    boardList=Guest.objects.all()
    
    return render(request,"board_app/index.html",{"board":board,"boardList":boardList})

