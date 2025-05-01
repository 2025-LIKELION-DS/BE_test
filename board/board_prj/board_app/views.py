from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST) #사용자가 쓴 폼 들고옴
        if form.is_valid: #폼 유효성 검사
            form.save() 
            return redirect('board_app:index') #자기자신으로 결과 보여줌
        
    else:
        form = GuestForm()

    form1=Guest.objects.all()

    return render(request,"board_app/index.html", {'form': form, 'form1': form1})

