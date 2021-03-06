from urlextract import URLExtract
import re

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
    contents = ("<b>Findings for " + fileName + ":</b><br/> <p>Network analysis findings: <br />" + "Potential URL's: <br />"
    + urlFindings + "<br /> Potential IP Addresses" + ipFindings + "<br /> Overall Scorecard is "
    + str(scorecard) + "<br /></p>")

    return contents

#network ability examples
#strings = getSectionStrings("7z.dll", 1, undesirables, False)
#getNetworkAbility(strings)