#multiclipboard

import shelve
import pyperclip
import sys

if(sys.argv[1] == 'save'):
    shelveFile = shelve.open("Clipbord.txt")
    shelveFile[sys.argv[2]] = pyperclip.paste()
    print("Data from clipboard saved to ",sys.argv[2])
    shelveFile.close()
if(sys.argv[1] == 'list'):
    shelveFile = shelve.open("Clipbord.txt")
    print(list(shelveFile.keys()))
    shelveFile.close()
if(sys.argv[1] == 'access'):
    shelveFile = shelve.open("Clipbord.txt")
    print(shelveFile[sys.argv[2]])
    shelveFile.close()
if(sys.argv[1] == 'retrive'):
    shelveFile = shelve.open("Clipbord.txt")
    pyperclip.copy(shelveFile[sys.argv[2]])
    print("Data retrived from ",sys.argv[2]," to clipboard")
    shelveFile.close()