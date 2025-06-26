from django.urls import path
from .views import *

app_name="lectures"

urlpatterns = [
    path('', index, name='index'),
    path('professor/', professor, name='professor'),
    path('lecture/', lecture, name='lecture'),
    path('student/', student, name='student')
]
