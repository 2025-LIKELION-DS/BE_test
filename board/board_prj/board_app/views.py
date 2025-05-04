from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestForm

def index(request):
    if request.method == 'GET':
        form = GuestForm()
        contents = Guest.objects.all()
        return render(request, 'board_app/index.html', {'form' : form, 'contents' : contents})
    
    form = GuestForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('board_app:index')