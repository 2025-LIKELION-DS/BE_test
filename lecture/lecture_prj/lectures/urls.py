from django.urls import path
from .views import *

app_name='lectures'

urlpatterns=[
    path('', index, name='index'),
    path('prof/', professor, name='professor'),
    path('lecture/', lecture, name='lecture'),
    path('stu/', student, name='student'),
]