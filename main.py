import pefile as pf
import os
import tkinter as tk 
import subprocess

from tkinter import Tk, StringVar
from tkinter import filedialog
from fileSig import file_Sig
from wrapResults import wrap_Results
from importExport import import_Export
from compileTime import compile_Time
from packedStatus import packed_Status
from unpack import unpack
from getStrings import getSectionStrings, getAllStrings
from networkAbility import network_Ability

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
    compileTime = ""

    #Open template file in original package directory first,
    #before switching to target directory

    with open('cssTemplate.txt', 'r') as templateFile:
        wrapper = templateFile.read()

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
    os.chdir(sourcePath)

    for root, subdir, files in os.walk(sourcePath):
        for file in files:
            if file.endswith(".exe"):
                pe = pf.PE(file)
                pe.parse_data_directories()
                impExpData += import_Export(pe, file)
                packedStatusData += packed_Status(pe, file)
    

    
    #fileSig(dir)
    #compileTime(dir)
    #based on the result of packedStatus/which packing manager is needed -> unpack(dir)
    #findStrings(dir) -> will need to identify the most out of these other functions, 
    # will likely need to return many strings. 
    # Based on the results of findStrings -> networkAbility(dir)
    #
    #Beyond these function calls, main should be fairly minimal, with perhaps some additional
    #error catch blocks included after function calls.

    #This function is subject to change, and will take data returned
    #from each module/function to be wrapped in a html file.
    wrap_Results("Report", impExpData, packedStatusData, wrapper)
    return

if __name__ == '__main__':
    main()