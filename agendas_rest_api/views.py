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

# Create your views here.
def home(request):
	contexto = {'vagas': 'lista'}
	return render(request, 'agendas_rest_api/index.html', contexto)


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
		return redirect('agendas_rest_api:home')



def getjson(request):
	message = "Resposta atualizada com sucesso"
	# verifica se a requisição foi feita via ajax
	if request.is_ajax(): 
		# cria um dicionário de dados a ser retornado para o cliente(browser)
		data = {'success': True, 'message': message, 'valor': 152}

		# converte os dados em json e retorna
		return HttpResponse(json.dumps(data), content_type='application/json')

	else:
		# se a requisição não é ajax, ela é direcionada para outra página
		contexto = {'resposta': 'respostass'}
		return redirect('agendas_rest_api:home')

def obterVagasPorMedico(request):
	if request.is_ajax():
		tuplas = [

			{'estabelecimento':'Hospital Jardim das Oliveiras', 'especialidade':'Dermatologia', 'medico':'Felipe Alcantara', 'vagas':14}, 
			{'estabelecimento':'Clínica menino Jesus', 'especialidade':'Pediatria', 'medico':'Alex Firmino', 'vagas':11},
			{'estabelecimento':'Pronto socorro Irineu', 'especialidade':'Clínica geral', 'medico':'Felipe Queiroz', 'vagas':25},
		]
		vagas = {'vagas':tuplas}
		return HttpResponse(json.dumps(vagas), content_type='application/json')






