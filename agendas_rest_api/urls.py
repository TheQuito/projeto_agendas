from django.contrib import admin
from django.urls import path, include
from . import views

#from rest_framework import routers
#router = routers.DefaultRouter()


app_name='agendas_rest_api'

urlpatterns = [
	#path('router', include(router.urls)),
	path('', views.dashboard, name='dashboard'),
	path('getVagasApp/', views.getVagasApp, name='getVagasApp'),
	path('agendamentosApp/', views.agendamentosApp, name='agendamentosApp'),
	path('atrasoMedioExames', views.atrasoMedioExames, name='atrasoMedioExames'),
	
	path('login/', views.login, name='login'),
	path('sair/', views.sair, name='sair'),
]
