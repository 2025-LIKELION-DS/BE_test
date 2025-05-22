from django.urls import path
from .views import *

app_name='lectures'

urlpatterns = [
    path('',home,name='home'),
    path('prof/',professor,name='professor'),
    path('lecture/',lecture,name='lecture'),
    path('stu/',student,name='student'),
]