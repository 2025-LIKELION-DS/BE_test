from django.urls import path
from .views import *

app_name='lectures'

urlpatterns = [
    path('', index, name='index'),
    path('prof/', prof, name='prof'),
    path('lecture/', lecture, name='lecture'),
    path('stu/', stu, name='stu'),
]