#Organising Files

import os,shutil

'''
os.chdir("E:\\")
shutil.copy("E:\\Python\\file.txt","C:\\Users\\avina\\OneDrive\\Desktop\\")
shutil.copytree("E:\\Python","C:\\Users\\avina\\OneDrive\\Desktop\\")
shutil.move("E:\\Python\\file.txt","C:\\Users\\avina\\OneDrive\\Desktop\\")

os.unlink(path)
os.rmdir(path)
os.rmtree(path)

'''

for folderName,subfolders,files in os.walk("E:\\Python"):
    print("Current folder is ",folderName)
    for subfolder in subfolders:
        print("Current subfolder in "+folderName+" is "+subfolder)
    for file in files:
        print("Current file in "+folderName+" is "+file)