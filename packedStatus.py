#Potential imports
'''
This function determines if this file is packed with UPX, or another, harder to detect, packing manager.
One of the most common giveaways of a file using UPX, is "SECTION UPX0" being part of the header information.
The "b" before most strings in the given output denotes that this is bytecode information.
'''
def packed_Status(portableExe, fileName): # -> return string or boolean identifying the packed status of file.
    
    if (hasattr(portableExe, "DIRECTORY_ENTRY_IMPORT")):
        for section in portableExe.sections:
            if (b'UPX0' in section.Name):
                print(fileName, "uses the following packing manager ->", section.Name, "\n")
                return   

            else:
                continue
    else:
         print(fileName, "has no detectable imports, it is likely packed with another manager such as FSG or ASPack.\n")

    return 
