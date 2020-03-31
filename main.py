import pefile as pf
import os
import sys
import tkinter as tk 
import subprocess

#External imports
from tkinter import Tk, StringVar, filedialog, messagebox

#Internal imports
from fileSig import fileSigMD5, fileSigSHA256
from compileTime import getCompileTime
from importExport import getImportExport
from packedStatus import getPackedStatus
from getStrings import getSectionStrings, getAllStrings
from networkAbility import getNetworkAbility
from riskAnalysis import getRiskAnalysis, getMatchCases
from wrapResults import wrapResults

'''
The main function in this file has the following tasks:
Establish empty string variables that will be exported to 'wrapResults'. These variables contain raw
information extracted from .exe files, and are hybridized with HTML formatting. Do not try to read 
raw string information in these files.
Establish a target directory from which information is read. Tkinter helps with this.
Run through this target directory, for each .exe file, execute the auxiliary functions to collect information.
Once all .exe files have been read, export all information to be wrapped into a web report.
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