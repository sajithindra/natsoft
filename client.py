import os
dirlist = os.listdir('.')
print(dirlist)
folder=[]
files = []
for i in dirlist:
    if '.' in i:
        files.append(i)
    else: folder.append(i)
print(folder)
print(files)