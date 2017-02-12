import os

def renameFiles():
    os.chdir("")
    file_list = os.listdir("");
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))

renameFiles()