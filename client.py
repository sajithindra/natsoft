import os
import requests
import json


def foldersync(path):
    dirlist = os.listdir(path)
    folder=[]
    files = []
    for i in dirlist:
        if '.' in i:
            files.append(i)
        else: folder.append(i)
    for i in folder:
        data={"folder" : [i]}
        r =requests.post("http://127.0.0.1:8000/folder",json = data)
        print (r.content)
    for i in files:
        url = 'http://127.0.0.1:8000/upload'
        files = [('files', open(i, 'rb'))]
        resp = requests.post(url=url, files = files) 
        print(resp.json())

foldersync(".")
