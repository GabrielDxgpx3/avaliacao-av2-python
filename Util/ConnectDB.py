import mysql.connector

class ConnectMySQL:
	usuario = "gabriel"
	senha ="####"
	host = "####"
	database = "prova_uniruy"

	def __init__(self):
		self.cursor = None
		self.connect()
	
	def connect(self):
		self.conexao = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.database)

	def getCursor(self):
		self.cursor = self.conexao.cursor(dictionary=True)
		return self.cursor;

	def closeCursor(self):
		return self.cursor.close()

	def commit(self):
		self.conexao.commit()
	
	def disconnect(self):
		self.closeCursor()
		self.conexao.close()	
