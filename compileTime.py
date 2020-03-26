import datetime
import time
def getCompileTime(portableExe, fileName):  # -> return string of compile time, if not found return "None found."
    contents = ""

    time_Stamp = str(datetime.datetime.utcfromtimestamp(portableExe.FILE_HEADER.TimeDateStamp))

    contents += str("<br /> Compile Time for " + fileName + " -> " + time_Stamp + "<br />") 


    return contents
