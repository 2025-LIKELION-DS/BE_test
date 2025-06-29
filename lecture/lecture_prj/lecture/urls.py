from django.urls import path
from .views import *

app_name = 'lecture'

urlpatterns = [
    path('', index, name='index'),
    path('prof/', professor_list, name='professor-list'),
    path('lecture', lecture, name='lecture-list'),
    path('stu/', student, name='student-list'),
]
