from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestBoardForm

def index(request):

    if request.method =="POST":
        form = GuestBoardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('board_app:index')
    else:
        form = GuestBoardForm()
    
    guests = Guest.objects.all()
    return render(request, 'board_app/index.html', {'guests': guests, 'form':form})