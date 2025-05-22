from django.contrib import admin
from .models import Lecture, Student, Professor

admin.site.register(Lecture)
admin.site.register(Student)
admin.site.register(Professor)