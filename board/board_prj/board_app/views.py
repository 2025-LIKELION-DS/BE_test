from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_app:index')
    else:
        form = GuestForm()
    
    guests = Guest.objects.all().order_by('-id')
    return render(request,'board_app/index.html',{'form' : form, 'guests': guests } )
