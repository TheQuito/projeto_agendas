from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# DEPENDÊNCIAS NECESSÁRIAS PARA IMPLEMENTAR A LOGIN
from django.contrib.auth import authenticate, logout, login as authlogin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

import json
from datetime import datetime, date, timedelta
import cx_Oracle
from agendas_rest_api.utils.conexao import Conexao
from agendas_rest_api.utils.querys import getQueryVagasApp
from agendas_rest_api.utils.datasUtil import obterListaDeDatas, getDia, getMes, getAno, getData
from agendas_rest_api.services.vagasApp import AgendamentosApp



# ########################### VIEWS DE LOGIN ##########################
def login(request):
	if request.user.id:
		return render(request, 'agendas_rest_api/dashboard.html',{})
	if request.POST:
		usuario = request.POST.get('usuario')
		senha = request.POST.get('senha')
		u = authenticate(request, username=usuario, password=senha)

		if(u is not None):
			if(u.is_active):
				authlogin(request, u)
				return redirect('agendas_rest_api:dashboard')

	return render(request, 'agendas_rest_api/login.html', {})

def sair(request):
	logout(request)
	#return redirect('agendas_rest_api: login')
	return render(request, 'agendas_rest_api/login.html', {})
# ########################### SISTEMA DE LOGIN ##########################



@login_required
def dashboard(request):
	return render(request, 'agendas_rest_api/dashboard.html', {})


def getVagasApp(request):
	if request.is_ajax():
		lista = AgendamentosApp().obterVagasDisponiveis()
		contexto = {'vagas': lista}
		return HttpResponse(json.dumps(contexto), content_type='application/json')
	else:
		contexto = {}
		return render(request, 'agendas_rest_api/vagasApp.html', {})


@login_required
def agendamentosApp(request):
	if request.user.has_perm('global_permissions.acessar_agendamentosApp'):
		if request.is_ajax():
			dataInicio = request.GET.get('dataInicio')
			dataFim = request.GET.get('dataFim')

			agendamentosApp = AgendamentosApp()

			if len(dataInicio.split('-')) > 1 and len(dataFim.split('-')) > 1: # is not None and dataFim is not None and estabelecimento is not None:
				dados = agendamentosApp.obterAgendamentosRealizados(getData(dataInicio), getData(dataFim))
				datas = obterListaDeDatas(date(getAno(dataInicio), getMes(dataInicio), getDia(dataInicio)), date(getAno(dataFim), getMes(dataFim), getDia(dataFim)), timedelta(days=1))
				contexto = {'agendamentos': dados, 'listaDeDatas': datas}
				return HttpResponse(json.dumps(contexto), content_type='application/json')
			else:
				hoje = datetime.now()
				inicioPeriodo = hoje - timedelta(15)
				param1 = str(inicioPeriodo.day) + '/' + str(inicioPeriodo.month) + '/' + str(inicioPeriodo.year)
				param2 = str(hoje.day) + '/' + str(hoje.month) + '/' + str(hoje.year)
				dados = agendamentosApp.obterAgendamentosRealizados(param1, param2)
				
				datas = obterListaDeDatas(date(inicioPeriodo.year, inicioPeriodo.month, inicioPeriodo.day), date(hoje.year, hoje.month, hoje.day), timedelta(days=1))
				contexto = {'agendamentos': dados, 'listaDeDatas': datas}
				return HttpResponse(json.dumps(contexto), content_type='application/json')
		else:
			return render(request, 'agendas_rest_api/agendamentosApp.html')

	else:
		return redirect('agendas_rest_api:dashboard')






