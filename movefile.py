import os, shutil

source = "/home/adilsheeth/Downloads/"
dest = "/home/adilsheeth/Documents"

listoffiles = os.listdir(source)

for file in listoffiles:
    root, ext = os.path.splitext(file)
    if(ext == ".pdf"):
        path = source + file
        shutil.move(path, dest)