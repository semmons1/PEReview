import pefile

'''
portExe -> portable executable in project folder
sectionNum -> the section number to get hash of
'''
def fileSectionSigMD5(portExe, sectionNum):
    section = portExe.sections[sectionNum]
    hash = section.get_hash_md5()
    print('Section name:', section.Name)
    print('MD5 hash:', hash)
    return hash

'''
portExe -> portable executable in project folder
sectionNum -> the section number to get hash of
'''
def fileSectionSigSHA256(portExe, sectionNum):
    section = portExe.sections[sectionNum]
    hash = section.get_hash_sha256()
    print('Section name:', section.Name)
    print('SHA256 hash: ', hash)
    return hash

'''
portExe -> portable executable in project folder
'''
def fileSigMD5(portExe):
    hash = ''
    for section in portExe.sections:
        tmpHash = section.get_hash_md5()
        print('Section name:', section.Name)
        print('MD5 hash: ', tmpHash)
        hash += tmpHash
    return hash

'''
portExe -> portable executable in project folder
'''
def fileSigSHA256(portExe):
    hash = ''
    for section in portExe.sections:
        tmpHash = section.get_hash_sha256()
        print('Section name:', section.Name)
        print('SHA256 hash: ', tmpHash)
        hash += tmpHash
    return hash