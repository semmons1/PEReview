import datetime
import time
def compile_Time(portableExe, fileName):  # -> return string of compile time, if not found return "None found."

    time_Stamp = datetime.datetime.utcfromtimestamp(portableExe.FILE_HEADER.TimeDateStamp)

    print("Compile Time:", time_Stamp)


    return
