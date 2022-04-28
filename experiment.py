from genericpath import isdir, isfile
import mimetypes
from ntpath import join
import os


uri='D:\\CS\\ComputerSystems-p3'
rd="bin\ls"
print(isfile(rd))
print(isdir(rd))
flag=0
for top, dirs, files in os.walk(uri):  
    if isdir(rd):
        print("entered 1st if") 
        for dir in dirs:
            print("searching for dir")
            ccp=os.path.join(top,dir)
            print(ccp)
            if  ccp.endswith(rd):
                flag=1
                print("directory exists")
                print("complete path: "+ccp)
                for files in os.listdir(ccp):
                    print(files)
            if flag==1: break
    if flag==1: break

    if isfile(rd):
        for file in files:
            ccp=os.path.join(top,file)
            if  ccp.endswith(rd):
                fileType=mimetypes.MimeTypes().guess_type(uri)[0]
                if fileType==None:
                    data=open(ccp,encoding="utf8").read()
                    exec(open(ccp).read())
                    print("file opened")
                    # exec(data)
                print("file found")
                flag=1
            if flag==1: break

    if flag==1: break
if flag==0:
            print("wrong path given")