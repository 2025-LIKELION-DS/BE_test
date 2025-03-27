from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def welcome(request):
    entered_name=request.GET['name']
    birthyear=request.GET['year']
    birthmonth=request.GET['month']
    birthday=request.GET['day']
    
    age=2025-int(birthyear)
    
    return render(request, "welcome.html",{"nametext":entered_name,"yeartext":birthyear,"monthtext":birthmonth,"daytext":birthday,"agetext":age})