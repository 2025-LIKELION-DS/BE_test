from django.contrib import admin
from .models import Professor, Lecture, Student
# Register your models here.

admin.site.register(Professor)
admin.site.register(Lecture)
admin.site.register(Student)