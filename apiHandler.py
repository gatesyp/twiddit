from __future__ import print_function
from alchemyapi_python.alchemyapi import AlchemyAPI
import json
import googleHandler
import redditHandler
def getData(filename):
	with  open('C:\\Users\\gatesyp\\Documents\\GitHub\\twiddit\\tweetsRepo\\' + filename + '.txt', 'r') as myfile:
		data = myfile.read().replace('\n', ' ')
	
	alchemyapi = AlchemyAPI()
	response = alchemyapi.entities('text', data, {'sentiment': 1})

	if response['status'] == 'OK':
		#print(json.dumps(response, indent=4))
		for entity in response['entities']:
			try:
				result = testGoog.searchGoog(entity['text'])
				
				if float(entity['relevance']) > 0.4:
					#print(result[0]['url'])
					#print(result[1]['url'])
					redditHandler.subscribe(result[0]['url'], mybiszti, lolipop123)
					redditHandler.subscribe(result[1]['url'], mybiszti, lolipop123)

			except:
				print("none or code 403")
