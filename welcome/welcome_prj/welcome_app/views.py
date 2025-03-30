from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'welcome_app/index.html')

def welcome(request):
    
    name=request.GET.get('name')
    year=request.GET.get('year')
    month=request.GET.get('month')
    day=request.GET.get('day')
    
    age = 2025 - int(year) + 1
    
    context = {
        'name':name,
        'year':year,
        'month':month,
        'day':day,
        'age':age
    }
    
    return render(request, 'welcome_app/welcome.html', context)