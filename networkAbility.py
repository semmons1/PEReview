from urlextract import URLExtract
import re
# Required modules: idna, uritools, appdirs
'''
string -> string possibly containing urls or ip addresses
'''
def getNetworkAbility(fileName, string):
    contents = ""
    extractor = URLExtract()
    urlFindings = str(extractor.find_urls(string))
    ipFindings = str(re.findall("(\d{1,3}\.){3}\d{1,3}", string))
    #Count each occurence of a complete IP address or URL with .split()
    scorecard = len(urlFindings.split()) + len(ipFindings.split())
    contents += ("Findings for " + fileName + ":<br/> Network analysis findings: <br />" + "Potential URL's: <br />"
    + urlFindings + "<br /> Potential IP Addresses" + ipFindings + "<br /> Overall Scorecard is "
    + str(scorecard) + "<br />")
    return contents

#network ability examples
#strings = getSectionStrings("7z.dll", 1, undesirables, False)
#getNetworkAbility(strings)