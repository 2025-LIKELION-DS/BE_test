from django.shortcuts import render

# Create your views here.
def index(request):
   
    return render(request, 'index.html')

def welcome(request):
    user_name = request.GET['username']
    year=int(request.GET['year'])
    month = int(request.GET['month'])
    day=int(request.GET['day'])

    age = 2025-year+1
    return render(request,'welcome.html', {'name':user_name, 'age': age, 'year': year, 'month':month, 'day':day})