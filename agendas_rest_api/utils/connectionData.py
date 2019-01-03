import cx_Oracle

# ESTA CLASSE DEVE SER EDITADA COM OS DADOS DE CONEXÃO
class ConnectionData:
	def __init__(self, arg):
		self.user = ''
		self.password = ''
		self.host = ''
		self.db = ''



	def __del__(self):
		del self

		
