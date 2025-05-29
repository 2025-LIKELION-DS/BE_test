from django.contrib import admin
from .models import Lecture, Student, Professor, LectureStudent

admin.site.register(Lecture)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(LectureStudent)