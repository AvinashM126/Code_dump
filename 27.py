import zipfile,os,shutil

os.chdir("D:")
newZip = zipfile.ZipFile("soft.zip",'w')
for foldername,subfolders,files in os.walk("D:\\Softwares"):
    for file in files:
        f1 = os.path.join(foldername, file)
        newZip.write(f1)
newZip.close()

newZip.extractall()
newZip.extract('file.extension','path')