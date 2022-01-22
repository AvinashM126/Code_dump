#Files

import os

print(os.path.join('C:','Windows','system32'))
print(os.getcwd())
os.chdir('C:\Windows')
print(os.getcwd())

print(os.path.isabs('.'))
print(os.path.isabs('C:\Windows'))

print(os.path.basename('C:\Windows\system32\calc.exe'))
print(os.path.dirname('C:\Windows\system32\calc.exe'))

calcFilePath = 'C:\Windows\system32\calc.exe'
print(os.path.split(calcFilePath))

print(os.path.getsize('E:\One Piece\Season_7 [196-228]\OP-226 LamBerT.mkv'))
print(os.path.getsize('E:\Python\21.py'))

Size = 0
for i in os.listdir('E:\Python'):
    Size += os.path.getsize(i)
#    print(i," : ",Size)
print("Total Size: ",Size)

os.makedirs('E:\Python\Test')
print(os.path.exists('E:\Python\Test'))
print(os.path.isdir('E:\Python\Test'))

print(os.path.isfile('E:\\Python\\21.py'))


f = open("E:\\Python\\file.txt")
print(f.read())
print(f.readline())
print(f.readlines())
f.close()


f = open('file1.txt','w')
f.write("This file is Overwritten")
f.close()