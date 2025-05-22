from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def professor_list(request):
    professor=Professor.objects.all()
    return render(request, 'professor_list.html', {"professor":professor})

def lecture_list(request):
    lecture=Lecture.objects.all()
    return render(request, 'lecture_list.html', {"lecture":lecture})

def student_list(request):
    student=Student.objects.all()
    return render(request, 'student_list.html', {"student":student})
