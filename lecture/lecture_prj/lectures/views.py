from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'lectures/index.html')

def professor(request):
    professor=Professor.objects.all().order_by('id')
    return render(request, 'lectures/professor_list.html', {'professor':professor})

def student(request):
    student=Student.objects.all().order_by('id')
    return render(request, 'lectures/student_list.html', {'student':student})

def lecture(request):
    lecture=Lecture.objects.all().order_by('id')
    return render(request, 'lectures/lecture_list.html',{'lecture':lecture})
