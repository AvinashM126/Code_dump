import pyperclip
import re

text = pyperclip.paste()
print(text)

print("\n\n\te-mail ID's:\n")
regEx = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')
print(regEx.findall(text))

print("\n\tPhone Nos:\n")
regExPh = re.compile(r'(\d)?\s\d\d\d.\d\d\d.\d\d\d\d')
phone = regExPh.finditer(text)
for i in phone:
    print("\t",i.group())
