#main.py

from __future__ import unicode_literals
from sql import databaseObj
from twitterWrapper import twitterApi







if __name__ == '__main__':
	db = databaseObj()
	#db.deleteTable('test')
	db.createTable('test', [ ['name', 'text'], ['username', 'text'], ['age', 'int']])
	db.insertIntoTable('test', ['bob', 'ace', 'clock'])
	res = db.queryDatabase()
	print res
	
	
	
	
	
	bot = twitterApi('twitter_credentials.txt')
	#message = "bingbong"
	#bot.post(message)