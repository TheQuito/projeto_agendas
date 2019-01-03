import cx_Oracle
from connectionData import ConnectionData 

class Conexao:

	global conn

	# Método construtor
	def __init__(self, user, password, host, db):
		connectionData = ConnectionData()
		self.user = connectionData.user
		self.password = connectionData.password
		self.host = connectionData.host
		self.db = connectionData.db

		try:
			

		super(Conexao, self).__init__()
		self.arg = arg


	# Método destrutor
	def __del__(self):
		del self
