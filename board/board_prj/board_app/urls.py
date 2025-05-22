from django.contrib import admin
from django.urls import path, include
from board_app import views

app_name = 'board_app'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name= 'index'),
]