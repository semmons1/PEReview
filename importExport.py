#Potential imports here
'''
This function tracks down any import and DLL information associated with a particular executable.
While it is not common, some executables will have an export directory, and this function will list them for you.
The "b" before most strings in the given output denotes that this is bytecode information.
'''
def import_Export(portableExe, fileName):

    if (hasattr(portableExe, "DIRECTORY_ENTRY_IMPORT")):
        print(fileName, "has the following imports: \n")
        for entry in portableExe.DIRECTORY_ENTRY_IMPORT:
            print(entry.dll)
            for imp in entry.imports:
                print('\t', hex(imp.address), imp.name)
    else:
        print(fileName, "does not contain any detectable imports. \n")

    if (hasattr(portableExe, "DIRECTORY_ENTRY_EXPORT")):
        print(fileName, "has the following exports: \n")
        for exp in portableExe.DIRECTORY_ENTRY_EXPORT:
            print(hex(portableExe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)

    else:
       print(fileName, "does not contain any detectable exports. \n")
    
    return