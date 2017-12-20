########### Python 2.7 #############
import httplib, urllib, base64
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '806c8090f88e482f8d00558b7d9a29db',
}

params = urllib.urlencode({
})


def getName(faceId):
	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("GET", "/face/v1.0/persongroups/group1/persons/%s?%s" % (faceId, params), "{body}", headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	data = json.loads(str(data))
	name = data["name"]
	return name