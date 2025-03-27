from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def welcome(request):
    name = request.GET['name']
    year = request.GET['year']
    month = request.GET['month']
    day = request.GET['day']

    age = 2025 - int(year) + 1

    return render(request, 'welcome.html', {'name': name, 'year': year, 'month': month, 'day': day, 'age': age})

