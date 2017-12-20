########### Python 2.7 #############
import httplib, urllib, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '806c8090f88e482f8d00558b7d9a29db',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion',
})

def detectFace():
    try:
        imageFile = open("image.jpg", "rb")
    except:
        print "Image File Not Valid or Available"
    f = imageFile.read()

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, f, headers)
        response = conn.getresponse()
        data = response.read()
    except:
        return -2, -2
    dataToRet = str(data)
    data = str(data)
    if data == "[]":
        return -1, -1
#    print data
    data = json.loads(data)
    faceId = str(data[0]["faceId"])
    conn.close()

    return faceId, dataToRet
