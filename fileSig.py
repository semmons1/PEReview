import hashlib

'''
portExe -> portable executable in project folder
blockSize -> amount of data to read to memory each iteration
          -> set to value of 65536 for default
'''
def fileSigMD5(portExe, blockSize):
    hash = hashlib.md5()
    with open(portExe, 'rb') as f:
        fb = f.read(blockSize)
        while len(fb) > 0:
            hash.update(fb)
            fb = f.read(blockSize)
    hash = hash.hexdigest()
    return hash

'''
portExe -> portable executable in project folder
blockSize -> amount of data to read to memory each iteration
          -> set to value of 65536 for default
'''
def fileSigSHA256(portExe, blockSize):
    hash = hashlib.sha256()
    with open(portExe, 'rb') as f:
        fb = f.read(blockSize)
        while len(fb) > 0:
            hash.update(fb)
            fb = f.read(blockSize)
    hash = hash.hexdigest()
    return hash

#Examples:
#print('sha256 hash:', fileSigSHA256('7z.dll', 65536))
#print('md5 hash:', fileSigMD5('7z.dll', 65536))