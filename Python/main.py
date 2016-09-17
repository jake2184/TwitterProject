#main.py

from sql import databaseObj
from twitterWrapper import twitterApi

import time


def processTweet(tweet):
	#print tweet
	pass

if __name__ == '__main__':
	db = databaseObj()
	#db.deleteTable('test')
	#db.createTable('test', [ ['name', 'text'], ['username', 'text'], ['age', 'int']])
	#db.insertIntoTable('test', ['bob', 'ace', 'clock'])
	#res = db.queryDatabase()
	#print res
	
	
	
	
	
	bot = twitterApi('twitter_credentials.txt')
	
	
	for line in bot.api.GetStreamFilter(track=['london']):
		print line['text'].encode('utf8') #+ '\n'
		processTweet(line)
		time.sleep(5)

		
		
