from django.shortcuts import render

# Create your views here.
def welcome(request):
    user_name=request.GET.get('user_name')
    year=request.GET.get('year')
    month=request.GET.get('month')
    day=request.GET.get('day')

    old=2025-int(year)+1
    
    return render(request,'welcome.html',{'name':user_name,'year':year,'month':month,'day':day,'old':old})

def index(request):
    return render(request,'index.html')