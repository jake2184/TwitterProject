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
		self.api = twitter.Api(	credentials['consumer_key'], \
								credentials['consumer_secret'],\
								credentials['access_token_key'],\
								credentials['access_token_secret'])
		
	
	def post(self, toPost):
		print 'posting ' + toPost 
		self.api.PostUpdate(toPost)
		print result.text