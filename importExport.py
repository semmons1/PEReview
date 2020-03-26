#Potential imports here
'''
This function tracks down any import and DLL information associated with a particular executable.
While it is not common, some executables will have an export directory, and this function will list them for you.
The "b" before most strings in the given output denotes that this is bytecode information.
'''
def getImportExport(portableExe, fileName):
    contents = ""

    if (hasattr(portableExe, "DIRECTORY_ENTRY_IMPORT")):
        contents += (fileName + " has the following dll's associated with it: <br />")
        for entry in portableExe.DIRECTORY_ENTRY_IMPORT:
            contents += str(entry.dll, 'utf-8')
            contents += str("<br /> This dll contains the following imports: <br />")
            for imp in entry.imports:
                tempAddress = str(hex(imp.address))
                tempName = str(imp.name, 'utf-8')
                contents += str(tempAddress + " -> " + tempName + "<br />")
    else:
        contents += str(fileName + " does not contain any detectable imports. <br />")

    if (hasattr(portableExe, "DIRECTORY_ENTRY_EXPORT")):
        contents += (fileName + " has the following exports: <br />")
        for exp in portableExe.DIRECTORY_ENTRY_EXPORT.symbols:
            tempAddressExp = str(hex(portableExe.OPTIONAL_HEADER.ImageBase + exp.address))
            tempNameExp = str(exp.name, 'utf-8')
            tempOrdinal = str(exp.ordinal)
            contents += str(tempAddressExp + " -> " + tempNameExp + " ordered @ " + tempOrdinal + "<br />")

    else:
       contents += str(fileName + " does not contain any detectable exports. <br />")
    
    return contents