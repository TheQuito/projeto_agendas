import cx_Oracle
from agendas_rest_api.utils.querys import  getTempoEsperaPorExame
from agendas_rest_api.utils.conexao import Conexao

class Exames:
    def __init__(self):
        pass

    def tempoEsperaPorExame(self):
        lista = []
        con = Conexao().obterConexao()
        cursor = con.cursor()
        cursor.execute(getTempoEsperaPorExame())
        for row in cursor:
            lista.append(row)
        con.close()
        return lista



