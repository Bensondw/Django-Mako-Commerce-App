import requests
import json

def GetItemInfo(item):
	
	url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=%s" %item

	req = requests.request('GET', url)

	results = req.json()


	try:
		return results[2][0]
	except:
		return 'description unavailable'
