import requests
import os
import re

'''
This function takes in raw data from both fileSig, and getStrings, and performs a simple
risk analysis based on the findings of these functions. Information is returned as string, to be wrapped.
'''
def getRiskAnalysis(fileName, hash):

    contents = ""
    #I know this is bad, works for now, will be replaced later!

    params = {'apikey': 'd335e195ea6f29e5df138840c4e40beac6bd997f37152b7c46a6846d8e86ffb9', 'resource' : hash}
    url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params = params)
    json_response = url.json()
    response = int(json_response.get('response_code'))
    if response == 0:
        contents += str("<p><b>" + hash + "(from " + fileName + ")" + "is not a registered signature. </b><br /></p>")
    elif response == 1:
        positives = int(json_response.get('positives'))
        if positives == 0:
            contents += str("<p><b>" + fileName + " is not registered as malicious with VirusTotal. </b><br /></p>")
        else:
            contents += str("<p><b>" + fileName + " is registered as malicious with VirusTotal because it has a hit count, please check hit count: </b></p>")
            contents += str(fileName + " has a hit count of " + str(positives) + "<br />")
    
    return contents

def getMatchCases(fileName, rawStringInfo):

    contents = ""
    scanString = rawStringInfo
    #This list could expand for a very long time, this is just what we've seen in our labs so far.

    catchValues = ['kernel', 'WARNING', '.com', '.dll', '.exe', 'http://', 'https://', 'DOS mode', 'API32', 'WININET', 'system32', 'ws2', 'wshtcpip']
    #Some regex magic later.
    #The main purpose of lines 30 & 31 is to set up a hashmap of values and patterns
    #that can be observed QUICKLY by the regex parsing engine. 

    pattern = r'\b({})\b'.format('|'.join(map(re.escape, catchValues)))
    matches = set(map(str.lower, re.findall(pattern, scanString, re.IGNORECASE)))

    tempHolder = str([x.upper() for x in catchValues if x.lower() in matches])
    contents += str("<b>This is only a snapshot of suspicious values parsed from raw string data in " + fileName + ", please look through the rest of this report: </b><br />" + tempHolder + "<br />") 
    
    return contents