from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome-app/', include('welcome_app.urls')),
]
