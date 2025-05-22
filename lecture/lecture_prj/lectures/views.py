from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'lectures/home.html')

def professor(request):
    professors=Professor.objects.all()
    return render(request,'lectures/professor_list.html',{'professors':professors})

def lecture(request):
    lectures=Lecture.objects.all()
    return render(request,'lectures/lecture_list.html',{'lectures':lectures})

def student(request):
    students=Student.objects.all()
    return render(request,'lectures/student_list.html',{'students':students})