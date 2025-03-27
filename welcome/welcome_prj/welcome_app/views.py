from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def welcome(request):
    birth_year=int(request.GET['year'])
    birth_month=int(request.GET['month'])
    birth_day=int(request.GET['day'])

    user_age=2025-birth_year+1
    user_name=request.GET['name']
    

    return render(request, 'welcome.html', 
                  {'age':user_age, 'year':birth_year, 'month':birth_month,
                   'day':birth_day, 'name':user_name})