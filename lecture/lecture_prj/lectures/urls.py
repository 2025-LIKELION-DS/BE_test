from django.urls import path
from .views import *

app_name = "lectures"
urlpatterns = [
    path('', index, name='index'),
    path('prof/', professor_list,name='professor_list' ),
    path('lecture/', lecture_list, name='lecture_list' ),
    path('stu/', student_list, name='student_list'),
]