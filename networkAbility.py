from urlextract import URLExtract
import re
# Required modules: idna, uritools, appdirs
'''
string -> string possibly containing urls or ip addresses
'''
def getNetworkAbility(string):
    extractor = URLExtract()
    urlFindings = extractor.find_urls(string)
    ipFindings = re.findall("(\d{1,3}\.){3}\d{1,3}", string)
    scorecard = len(urlFindings) + len(ipFindings)
    #print('Network ability scorecard:', scorecard)
    #print('Potential urls:', urlFindings)
    #print('Potential ip addresses:', ipFindings)
    return scorecard

#network ability examples
#strings = getSectionStrings("7z.dll", 1, undesirables, False)
#getNetworkAbility(strings)