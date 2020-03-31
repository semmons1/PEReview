import os
import sys
import webbrowser

def wrapResults(fileName, ieInfo, pInfo, timeInfo, netInfo, analysisInfo, matchCaseInfo):


    setImportExportWrapper("pyIE", ieInfo)
    setPackedwrapper("pyPacked", pInfo)
    setNetworkAbilityWrapper("pyNetwork", netInfo)

    with open('pyHome.txt', 'r') as homeFile:
        wrapper = homeFile.read()

    outFilename = fileName + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (matchCaseInfo, analysisInfo, timeInfo)
    outFile.write(rawContentTransfer)
    outFile.close()

    print("Opening page now...")

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


def setNetworkAbilityWrapper(fileName, nInfo):
    with open('pyNetwork.txt', 'r') as netFile:
        wrapper = netFile.read()

    outFilename = fileName + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (nInfo)
    outFile.write(rawContentTransfer)
    outFile.close()

    return
