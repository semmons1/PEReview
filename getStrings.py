import pefile
import re

'''
fileName -> name of file in project folder
sectionNum -> the section's index number
filterList -> list of raw strings to filter out
isSplit -> split string in list of strings by whitespace if True
'''
def getSectionStrings(fileName, sectionNum, filterList, isSplit):
    pe = pefile.PE(fileName)
    strings = str(pe.sections[sectionNum].get_data()[:])
    for word in filterList:
        strings = re.sub(word, '', strings)
    if isSplit: strings = strings.split()
    print(strings)
    return strings

'''
fileName -> name of file in project folder
filterList -> list of raw strings to filter out
isSplit -> split string in list of strings by whitespace if True
'''
def getAllStrings(fileName, isSplit):
    undesirables = [r'\\x\w{2}', r'\\', r'\@', r'\#', r'\!', r'\$', r'\%']
    pe = pefile.PE(fileName)   
    strings = ""
    for section in pe.sections:
        strings += str(section.get_data()[:])
    for word in undesirables:
        strings = re.sub(word, '', strings)
    #.split() can be used if we wish to return an array instead. For now,
    #we only want raw string information.
    if isSplit: strings = strings.split()
    return strings

'''
undesirables = [r'\\x\w{2}', r'\\', r'\@', r'\#', r'\!', r'\$', r'\%']
getSectionStrings("7z.dll", 1, undesirables, True)
getAllStrings("7z.dll", undesirables, True)
'''