from datetime import datetime
import cx_Oracle
from agendas_rest_api.utils.querys import  getQueryVagasApp, getQueryAgendamentosRealizados
from agendas_rest_api.utils.conexao import Conexao

class AgendamentosApp:
    def __init__(self):
        self.inicio_periodo = datetime.now().strftime('%d/%m/%Y')
        self.fim_periodo = ''
        self.status_agenda = 'L'
        self.especialidades = '3'
        self.query = ''


    def obterVagasDisponiveis(self):
        lista = []
        con = Conexao().obterConexao()
        cursor = con.cursor()
        cursor.execute(getQueryVagasApp())
        for row in cursor:
            lista.append(row)
        con.close()
        return lista

    
    def obterAgendamentosRealizados(self, dataInicio, dataFim):
        especialidades = ['49', '3']  # ler as especialidades de um arquivo
        con = Conexao().obterConexao()
        cursor = con.cursor()
        lista = []
        masterLista = []
        
        for especialidade in especialidades:
            cursor.execute(getQueryAgendamentosRealizados(especialidade, dataInicio, dataFim))
            lista.clear()
            for agendamento in cursor:
                lista.append({'especialidade': agendamento[0], 'data': agendamento[1], 'qtd':agendamento[2]})
            masterLista.append(lista.copy())
            
        con.close()
        return masterLista
        