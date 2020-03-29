import requests
import os

def getRiskAnalysis(fileName, hash):
    contents = ""
    #I know this is bad, works for now, will be replaced later!
    params = {'apikey': 'd335e195ea6f29e5df138840c4e40beac6bd997f37152b7c46a6846d8e86ffb9', 'resource' : hash}
    url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params = params)
    json_response = url.json()
    response = int(json_response.get('response_code'))
    if response == 0:
        contents += str(hash + "(from " + fileName + ")" + "is not a registered signature. <br />")
    elif response == 1:
        positives = int(json_response.get('positives'))
        if positives == 0:
            contents += str(fileName + " is not registered as malicious with VirusTotal. <br />")
        else:
            contents += str(fileName + " is registered as malicious with VirusTotal because it has a hit count, please check hit count: <br />")
            contents += str(fileName + " has a hit count of " + str(positives) + "<br />")
    return contents
