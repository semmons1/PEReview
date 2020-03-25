import pefile
import re

'''
fileName -> name of file in project folder
sectionNum -> the section's index number
filterList -> list of raw strings to filter out
'''
def getSectionStrings(fileName, sectionNum, filterList):
    pe = pefile.PE(fileName)  
    strings = str(pe.sections[sectionNum].get_data()[:])
    for word in filterList:
        strings = re.sub(word, '', strings)
    print(strings)
    return strings

'''
fileName -> name of file in project folder
filterList -> list of raw strings to filter out
'''
def getAllStrings(fileName, filterList):
    pe = pefile.PE(fileName)   
    strings = ""
    for section in pe.sections:
        strings += str(section.get_data()[:])
    for word in filterList:
        strings = re.sub(word, '', strings)
    print(strings)
    return strings

#example
undesirables = [r'\\x\w{2}', r'\\', r'@']
getSectionStrings("7z.dll", 1, undesirables)
#getAllStrings("7z.dll", undesirables)