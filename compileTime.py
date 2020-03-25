import datetime
import time
def compile_Time(portableExe, fileName):  # -> return string of compile time, if not found return "None found."
    contents = ""

    time_Stamp = datetime.datetime.utcfromtimestamp(portableExe.FILE_HEADER.TimeDateStamp)

    contents += str("<br /> Compile Time:" + time_Stamp + "<br />") 


    return contents
