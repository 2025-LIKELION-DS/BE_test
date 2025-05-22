from django.urls import path
from lectures import views

app_name='lectures'

urlpatterns = [
    path('',views.index,name="index"),
    path('professor-list/',views.professor_list,name="professor-list"),
    path('lecture-list/',views.lecture_list,name="lecture-list"),
    path("student-list/",views.student_list,name="student-list"),
]
