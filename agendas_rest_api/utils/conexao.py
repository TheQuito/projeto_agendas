import cx_Oracle
from agendas_rest_api.utils.connectionData import ConnectionData 

class Conexao:

	global conn

	# Método construtor
	def __init__(self):
		connectionData = ConnectionData()
		self.user = connectionData.user
		self.password = connectionData.password
		self.host = connectionData.host
		self.db = connectionData.db
		self.conn = None


	# Método responsável por retornar a conexão para o usuário
	def obterConexao(self):
		try:
			conn = cx_Oracle.connect(self.user+'/'+self.password+'@'+self.host+'/'+self.db)
			return conn
		except:
			print('Erro ao conectar no banco')



	# Método destrutor
	def __del__(self):
		del self


   

        
        

   
         
        
    