import pefile
#Potential imports
def find_Strings(portExe): # -> return strings of interest found the executable
    print([entry.id for entry in portExe.DIRECTORY_ENTRY_RESOURCE.entries])
    strings = list()
    
    rt_string_idx = [entry.id for entry in portExe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_STRING'])
    rt_string_directory = portExe.DIRECTORY_ENTRY_RESOURCE.entries[rt_string_idx]

    for entry in rt_string_directory.directory.entries:
        data_rva = entry.directory.entries[0].data.struct.OffsetToData
        size = entry.directory.entries[0].data.struct.Size
        print('Directory entry at RVA', hex(data_rva), 'of size', hex(size))
        data = portExe.get_memory_mapped_image()[data_rva:data_rva+size]
        offset = 0
        while True:
            if offset>=size:
                break
            ustr_length = portExe.get_word_from_data(data[offset:offset+2], 0)
            offset += 2
            if ustr_length==0:
                continue
            ustr = portExe.get_string_u_at_rva(data_rva+offset, max_length=ustr_length)
            offset += ustr_length*2
            strings.append(ustr)
            print('String of length', ustr_length, 'at offset', offset)
            return strings
            
'''
This was an example done on a copy of the .dll file in 7zip
pe = pefile.PE("7z.dll")
foundStrings = find_Strings(pe)
encoding = 'utf-8'
for strs in foundStrings:
    print(strs.decode(encoding), "\n")
'''