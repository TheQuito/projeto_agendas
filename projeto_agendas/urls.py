"""projeto_agendas URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('agendas_rest_api/', include('agendas_rest_api.urls')),
]