#main.py

from __future__ import unicode_literals
from sql import queryDatabase
from twitterWrapper import twitterApi







if __name__ == '__main__':
	queryDatabase()
	
	bot = twitterApi('twitter_credentials.txt')
	print 'posting2'
	bot.post('wassup')