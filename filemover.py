from typing import Optional
from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
import os
app = FastAPI()

################################ Data model for the file structure #################################

class FileModel(BaseModel):
    folder : list =[]

###################### API for creating folers ##########################
@app.post("/")
async def filedata(data:FileModel):
    for i in data.folder:
        try: 
            os.mkdir(i)
        except FileExistsError:
            return {'Error': "File already exists"}
        else:
            dreturn {"Msg": "folder created sucessfully"}

###################### data model for file upload ###################################

@app.post("/fileupload")
async def fu(file:UploadFile = File (...),path='.'):
    filename = path+file.filename
    f=open(filename,'wb')
    content =await file.read()
    f.write(content)
    return "file uploaded "
