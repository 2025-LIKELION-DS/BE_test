from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'lectures/index.html')

def prof(request):
    professors = Professor.objects.all()
    return render(request, 'lectures/professor_list.html',{'professors':professors})

def lecture(request):
        lectures = Lecture.objects.all()
        return render(request, 'lectures/lecture_list.html',{'lectures':lectures})

def stu(request):
        students = Student.objects.all()
        return render(request, 'lectures/student_list.html',{'students':students})