from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    return render(request, 'welcome_app/index.html')

def welcome(request):
    entered_name = request.GET['name']
    entered_year = int(request.GET['year'])
    entered_month = int(request.GET['month'])
    entered_day = int(request.GET['day'])

    today = datetime.date.today()
    today_year = today.year
    age = today_year - entered_year + 1

    return render(request, 'welcome_app/welcome.html',{"entered_name" : entered_name, "entered_year" : entered_year, "entered_month" : entered_month, "entered_day" : entered_day, "age" : age})