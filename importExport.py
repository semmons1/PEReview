
'''
This function tracks down any and all imports/exports associated with a .exe file.
This information is then returned in string form, with HTML formatters injected.
@contents, Establish empty string variable, each time this function is called.
'''
def getImportExport(portableExe, fileName):
    
    contents = ""

    if (hasattr(portableExe, "DIRECTORY_ENTRY_IMPORT")):
        contents += ("<b><p>" + fileName + " has the following imports/dll's associated with it: <br /></p></b>")
        for entry in portableExe.DIRECTORY_ENTRY_IMPORT:
            contents += str(entry.dll, 'utf-8')
            contents += str("<br /> This dll contains the following imports: <br />")
            for imp in entry.imports:
                tempAddress = str(hex(imp.address))
                tempName = str(imp.name, 'utf-8')
                contents += str(tempAddress + " -> " + tempName + "<br />")
    else:
        contents += str("<b>" + fileName + " does not contain any detectable imports. <br /></b>")

    if (hasattr(portableExe, "DIRECTORY_ENTRY_EXPORT")):
        contents += ("<b><p>" + fileName + " has the following exports: <br /></p></b>")
        for exp in portableExe.DIRECTORY_ENTRY_EXPORT.symbols:
            tempAddressExp = str(hex(portableExe.OPTIONAL_HEADER.ImageBase + exp.address))
            tempNameExp = str(exp.name, 'utf-8')
            tempOrdinal = str(exp.ordinal)
            contents += str(tempAddressExp + " -> " + tempNameExp + " ordered @ " + tempOrdinal + "<br />")

    else:
       contents += str("<b>" + fileName + " does not contain any detectable exports. <br /></b>")
    
    return contents