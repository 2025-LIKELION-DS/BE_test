from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('create-review/<int:book_id>/', create_review, name='create-review'),
]

