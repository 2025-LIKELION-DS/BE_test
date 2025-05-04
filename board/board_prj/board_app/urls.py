from django.urls import path
from .views import index

app_name = 'board_app'

urlpatterns = [
    path('', index, name='index'),
]
