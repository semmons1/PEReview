import pefile
import re

'''
fileName -> name of file in project folder
sectionNum -> the section's index number
'''
def getStrings(fileName, sectionNum):
    pe = pefile.PE(fileName)   
    chars = str(pe.sections[sectionNum].get_data()[:])
    char_array = ""
    for c in chars: char_array += c
    print(re.sub(r'\\x\w{2}', '', char_array))
    return

# Example: Make sure you have a copy of the .dll
#          file from 7zip application for this 
#          to work correctly, or use any pe file!
# getStrings("7z.dll", 1)