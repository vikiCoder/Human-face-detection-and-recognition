########### Python 2.7 #############
import httplib, urllib, base64, json
import detect
import faceName

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '806c8090f88e482f8d00558b7d9a29db',
}

params = urllib.urlencode({
})

def Identify():
	faceId, faceData = detect.detectFace()
	if faceId == -1 or faceData == -1:
		return -1
	if faceId == -2 or faceData == -2:
                return -2
	body = {"personGroupId" : "group1", "faceIds" : [faceId], "maxNumOfCandidatesReturned" : 1, "confidenceThreshold" : 0.5}
	body = json.dumps(body)
	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/face/v1.0/identify?%s" % params, body, headers)
	response = conn.getresponse()
	data = response.read()
	data = json.loads(str(data))[0]
	if data["candidates"] != []:
                candidates = data["candidates"][0]
                faceId = candidates["personId"]
                conf = candidates["confidence"]
                name = faceName.getName(faceId)
        else:
                name = 'Unknown Person'
                conf = 0
        
	conn.close()
	
	faceData = json.loads(faceData)[0]
	del faceData['faceId']
	del faceData['faceRectangle']
	faceData.update({'confidence':conf,'name':name})
	faceAttr = faceData['faceAttributes']
	del faceData['faceAttributes']
	faceData.update(faceAttr)
	return faceData
