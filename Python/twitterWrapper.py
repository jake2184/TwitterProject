#twitterWrapper.py

import twitter

class twitterApi:
	def __init__(self, fileName):
		# Get twitter api credentials
		with open(fileName) as credentialFile:
			lines = credentialFile.readlines()
			credentials = {}
			for line in lines:
				credential = line.split('=')
				credentials[credential[0]] = credential[1].strip()
			print credentials
		self.api = twitter.Api(consumer_key=[credentials['consumer_key']], \
						consumer_secret=[credentials['consumer_secret']],\
						access_token_key=[credentials['access_token_key']],\
						access_token_secret=[credentials['access_token_secret']])
		print self.api
		
	
	def post(self, toPost):
		print 'posting'
		result = self.api.PostUpdate(toPost)
		print result.text