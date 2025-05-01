from django.contrib import *
from django.urls import path,include
from .views import *

app_name='board_app'

urlpatterns = [
    path('', index, name='index'),
]
