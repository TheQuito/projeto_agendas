from django.urls import path, include
from . import views

from rest_framework import routers
#from classifier.views import ClasseViewSet

router = routers.DefaultRouter()



app_name='agendas_rest_api'

urlpatterns = [
	#path('router', include(router.urls)),
	path('', views.dashboard, name='dashboard'),
	path('home', views.home, name='home'),
	path('getjson/', views.getjson, name='getjson'),
	path('obterVagas/', views.obterVagasPorMedico, name='obterVagas'),
	path('getVagasApp/', views.getVagasApp, name='getVagasApp'),
	
	
]
