import pefile
import re

'''
RETURNS STRINGS FROM A SINGLE SECTION
    fileName -> name of file in project folder
    sectionNum -> the section's index number
'''
def getSectionStrings(fileName, sectionNum):
    pe = pefile.PE(fileName)   
    chars = str(pe.sections[sectionNum].get_data()[:])
    char_array = ""
    for c in chars: char_array += c
    secStrs = re.sub(r'\\x\w{2}', '', char_array)
    #print(secStrs)
    return secStrs

'''
RETURNS STRINGS FROM ALL SECTIONS
    fileName -> name of file in project folder
'''
def getAllStrings(fileName):
    pe = pefile.PE(fileName)   
    chars = ""
    for section in pe.sections:
        chars += str(section.get_data()[:])
    char_array = ""
    for c in chars: 
        char_array += c
    fileStrs = re.sub(r'\\x\w{2}', '', char_array)
    #print(fileStrs)
    return fileStrs

#example
#getSectionStrings("7z.dll", 1)
#getAllStrings("7z.dll")