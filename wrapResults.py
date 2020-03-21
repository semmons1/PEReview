import os
import sys
import webbrowser

def wrap_Results(fname, ieInfo, pInfo, wrapper):

    outFilename = fname + '.html'
    outFile = open(outFilename, 'w')

    rawContentTransfer = wrapper % (ieInfo, pInfo)
    outFile.write(rawContentTransfer)
    outFile.close()
    print("File written!")

    path = os.path.abspath(outFilename)
    url = 'file://' + path
    webbrowser.open(url) #use default browser, to avoid issues with individual user preferences.

    return