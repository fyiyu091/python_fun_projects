import os
import re

def change_line_in_file(filename, pattern: str, replacement: str):
    lines = []
    with open(filename, 'r') as myfile:
        for line in myfile.readlines():
            if re.match(pattern, line):
                lines.append(replacement)
            else:
                lines.append(line)
    
    with open(filename, 'w') as myfile:
        myfile.writelines(lines)

def change_files_name(oldname: str, newname: str):
    file_list = os.listdir()
    for filename in file_list:
        if filename == oldname:
            os.rename(filename, newname)
