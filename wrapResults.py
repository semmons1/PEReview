import os
import sys
import webbrowser

def wrap_Results(fileName, ieInfo, pInfo, timeInfo):


    setImportExportWrapper("pyIE", ieInfo)
    setPackedwrapper("pyPacked", pInfo)

    with open('pyHome.txt', 'r') as homeFile:
        wrapper = homeFile.read()

    outFilename = fileName + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (timeInfo , "Other info")
    outFile.write(rawContentTransfer)
    outFile.close()

    print("File written!")

    path = os.path.abspath(outFilename)
    url = 'file://' + path
    webbrowser.open(url) #use default browser, to avoid issues with individual user preferences.

    return

def setImportExportWrapper(fileName, ieInfo):

    with open('pyIE.txt', 'r') as ieFile:
        wrapper = ieFile.read()

    outFilename = fileName + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (ieInfo)
    outFile.write(rawContentTransfer)
    outFile.close()

    return

def setPackedwrapper(fileName, pInfo):

    with open('pyPacked.txt', 'r') as pFile:
        wrapper = pFile.read()

    outFilename = fileName + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (pInfo)
    outFile.write(rawContentTransfer)
    outFile.close()

    return
