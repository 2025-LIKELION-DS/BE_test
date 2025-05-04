from django.shortcuts import render, redirect
from .forms import Form
from .models import Guest

def index(request):
    form=Form() # 빈 폼 생성
    if request.method=="POST": # 방명록 작성
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        # username = request.Guest.get('username') 대신 form

        # guest=Guest.objects.create(
        #     username='username',
        # )
    # return render(request, '/index.html', {'form':form}) # forms X form o
        return redirect('board_app:index') # 리턴 대신 리다이렉트

    if request.method == "GET": # 방명록 목록
        # pass
        guests=Guest.objects.all()
        return render(request, 'board_app/index.html', {'guests':guests, 'form':form})

