from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),
    path('', lambda request: redirect('film_list')),  # Добавьте этот маршрут
]