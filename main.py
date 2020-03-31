import pefile as pf
import os
import sys
import tkinter as tk 
import subprocess

from tkinter import Tk, StringVar
from tkinter import filedialog, messagebox
from fileSig import fileSigMD5, fileSigSHA256
from wrapResults import wrapResults
from importExport import getImportExport
from compileTime import getCompileTime
from packedStatus import getPackedStatus
from getStrings import getSectionStrings, getAllStrings
from networkAbility import getNetworkAbility
from riskAnalysis import getRiskAnalysis, getMatchCases

'''
The main function in this file has the following tasks:
@currentWorkingDir, the object that your current working directory is assigned to. 
@pe will pass file/directory information to relevant file analysis functions.
This tool should be in the same directory as potentially malicious executables.
This allows for the OS module to scan your directory for all .exe files.
This function should also contain checks (conditional, try blocks) for files that don't exist or are malformed.
After checks, parse the data directories, and ship them off to relevant functions. These functions will 
display relevant information about each executable being examined.
'''
def main():
    impExpData = ""
    packedStatusData = ""
    compileTimeData = ""
    rawStringData = ""
    networkAbilityData = ""
    riskAnalysisData = ""
    matchCaseData = ""
    packageDir = ""

    packageDir = os.getcwd()

    #Open template file in original package directory first,
    #before switching to target directory

    #with open('cssTemplate.txt', 'r') as templateFile:
    #    wrapper = templateFile.read()

    # This section allows the user to change the working directory
    # with a simple GUI. Ideally, the user will be in a Windows environment.
    # However, this should accept Linux and Mac folder paths with a slight modification 
    # to the 'initialdir' option.

    root = Tk()
    root.withdraw()
    folderPath = StringVar()
    source = filedialog.askdirectory(initialdir = "/", title = "Select Desired Directory")
    folderPath.set(source)
    sourcePath = folderPath.get()
    if os.path.exists(sourcePath) == True and sourcePath != "/":
        os.chdir(sourcePath)
        for root, subdir, files in os.walk(sourcePath):
            for file in files:
                if file.endswith(".exe"):
                    pe = pf.PE(file)
                    pe.parse_data_directories()
                    compileTimeData += getCompileTime(pe, file)
                    md5Signature = fileSigMD5(file, 65536)
                    impExpData += getImportExport(pe, file)
                    packedStatusData += getPackedStatus(pe, file)
                    rawStringData += getAllStrings(file, [], False)
                    networkAbilityData += getNetworkAbility(file, rawStringData)
                    riskAnalysisData += getRiskAnalysis(file, md5Signature) 
                    matchCaseData += getMatchCases(file, rawStringData)

    #This function is subject to change, and will take data returned
    #from each module/function to be wrapped in a html file.

        os.chdir(packageDir + "/htmlElements")
   
        wrapResults("pyHome", impExpData, packedStatusData, compileTimeData, networkAbilityData, riskAnalysisData, matchCaseData)
        return
    else:
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Invalid Directory", "Please check your directory, and try again.")
        SystemExit



if __name__ == '__main__':
    main()