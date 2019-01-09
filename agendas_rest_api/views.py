from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import json
import cx_Oracle
from agendas_rest_api.utils.conexao import Conexao
from agendas_rest_api.utils.querys import vagasAplicativo


def dashboard(request):
	return render(request, 'agendas_rest_api/dashboard.html', {})


def getVagasApp(request):
	if request.is_ajax():
		lista = []
		#con = cx_Oracle.connect('system/123456@localhost/XE')
		con = Conexao().obterConexao()
		cursor = con.cursor()
		cursor.execute(vagasAplicativo)
		for row in cursor:
			lista.append(row)
		contexto = {'vagas': lista}
		con.close()

		return HttpResponse(json.dumps(contexto), content_type='application/json')
	else:
		contexto = {}
		#return redirect('agendas_rest_api:getVagasApp')
		return render(request, 'agendas_rest_api/vagasApp.html', {})









