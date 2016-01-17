import urllib.parse
import urllib.request
import json as m_json
import sys

def searchGoog(term):
	print(term)
	query = "site:reddit.com " + term
	query = urllib.parse.urlencode ( { "q" : query } )
	response = urllib.request.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json = m_json.loads ( response.decode('utf-8' ))
#	print (m_json.dumps(json, indent=4, sort_keys=True))
	try:
		results = json [ 'responseData' ] [ 'results' ]
		#print(results[0]['url'])
		#print(results[1]['url'])
		return results
	except:
		#print("no result for 0")
		results = 0
		return 	results	



#searchGoog(sys.argv[1])
