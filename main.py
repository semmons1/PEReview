import pefile as pf
import os
import glob

from fileSig import file_Sig
from importExport import import_Export
from compileTime import compile_Time
from packedStatus import packed_Status
from unpack import unpack
from findStrings import find_Strings
from networkAbility import network_Ability

#Scan dir for exe's, and print the results to be sure.
def main():
    #Double forward slashes needed for escape sequence
    for filename in glob.iglob('C:\\Users\\ur_bad_malware_here\\*.exe'):
        pe = pf.PE(filename)
        pe.parse_data_directories()
        print('%x' % pe.FILE_HEADER.NumberOfSections)
    

    #Establish directory with malware files and assign to object.
    #Easiest option is to hardcode directory, but could also scan for for
    #directories labeled "malware".

    #use this new object as an argument to be passed to the following function calls, potential
    #return values will be listed in the function file.

    #fileSig(dir)
    #importExport(dir)
    #compileTime(dir)
    #packedStatus(dir)
    #based on the result of packedStatus/which packing manager is needed -> unpack(dir)
    #findStrings(dir) -> will need to identify the most out of these other functions, 
    # will likely need to return many strings. 
    # Based on the results of findStrings -> networkAbility(dir)
    #
    #Beyond these function calls, main should be fairly minimal, with perhaps some additional
    #error catch blocks included after function calls.
    print("Main is live.")
    return

if __name__ == '__main__':
    main()
  