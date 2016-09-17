#sql.py

import sqlite3

def stringifyCol(columns):
	toString = ""
	for tuple in columns:
		toString += tuple[0] + " " + tuple[1] + ", "
	return toString[:-2]

def stringifyVal(values):
	toString = ""
	for value in values:
		toString += "'" + value + "',"
	return toString[:-1]

class databaseObj:

	def __init__(self):
		self.initialise()

	def initialise(self):
		self.connection = sqlite3.connect('database.db')
		self.cursor = self.connection.cursor()
		
	def createTable(self, name, columns):
		self.cursor.execute("CREATE TABLE if not exists " + name + "(" + stringifyCol(columns) +")")
		self.connection.commit()	
	
	def deleteTable(self, name):
		toDo = "DROP TABLE IF EXISTS " + name
		#print toDo
		self.arbSQL(toDo)
		
	def insertIntoTable(self, tableName, values):
		toDo = "INSERT INTO " + tableName + " VALUES (" + stringifyVal(values) +")"
		#print toDo
		self.arbSQL(toDo)

	def queryDatabase(self):
		self.cursor.execute("SELECT * FROM test")
		return self.cursor.fetchall()
		
	def arbSQL(self, query):
		self.cursor.execute(query)
		self.connection.commit()
		return self.cursor.fetchall()
		
	