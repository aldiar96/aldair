import pymysql

class Data:

	def __init__(self):
		self.conn = pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="registro"
			)

		self.cursor = self.conn.cursor()



	def InsertItems(self, element):
		
		sql = "insert into veiculo(Nombre, ) values('{}')".format(element[0])
		
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios



	def ReturnOneItem(self, ref):
		#tenemos ref como el nombre del elemento
		sql = "select * from veiculo where Nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		#devolver el elemento o nulo

		return self.cursor.fetchone()


	def returnAllElements(self):
		sql = "select * from veiculo"
		self.cursor.execute(sql)
		return self.cursor.fetchall()


	def Delete(self, ref):
		sql = "delete from veiculo where Nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		self.conn.commit()


	def UpdateItem(self, element, ref):
		#El elemento contiene los valores y ref es el nombre del elemento que queremos cambiar.
		sql = "update veiculo set Nombre = '{}', where Nombre = '{}'".format(element[0] ref)
		#ejecutar la consulta
		self.cursor.execute(sql)
		self.conn.commit()#guardamos cambios




'''
d = Data()		
users = d.returnAllElements()
for i in users:
	print(i)
''' 