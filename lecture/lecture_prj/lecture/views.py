from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'lecture/index.html')

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'lecture/professor_list.html', {'professors':professors})

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture/lecture_list.html', {'lectures':lectures})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'lecture/student_list.html', {'students':students})




