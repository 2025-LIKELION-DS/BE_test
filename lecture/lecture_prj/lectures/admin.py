from django.contrib import admin
from .models import Professor, Lecture, Student, StudentLecture
# Register your models here.

admin.site.register(Professor)
admin.site.register(Lecture)
admin.site.register(Student)
admin.site.register(StudentLecture)