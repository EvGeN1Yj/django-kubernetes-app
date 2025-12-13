"""
URL configuration for django_app project.
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import socket

def get_hostname():
    return socket.gethostname()

def home(request):
    """Главная страница с информацией о pod'е"""
    return JsonResponse({
        'message': 'Django Kubernetes App',
        'hostname': get_hostname(),
        'status': 'running'
    })

def health(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'healthy', 'hostname': get_hostname()})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name='health'),
    path('', home, name='home'),
]

