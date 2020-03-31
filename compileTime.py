import datetime
import time

'''
This function collects timestamp information, and returns this information as a string.
@contents, Establish empty string variable, each time this function is called.
'''
def getCompileTime(portableExe, fileName):
    contents = ""

    time_Stamp = str(datetime.datetime.utcfromtimestamp(portableExe.FILE_HEADER.TimeDateStamp))

    contents += str("<br /> Compile Time for " + fileName + " -> " + time_Stamp + "<br />") 

    return contents
