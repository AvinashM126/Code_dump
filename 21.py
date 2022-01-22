# Regular Expression

'''
\d  Numeric digit 0 - 9
\D  ~ \d
\w  Letter, numeric or underscore
\W  ~ \w
\s  Space tab or newline
\S  ~ \s

'''
import re
s = "Batman drives a batmobile"
s1 = "Batwoman drives a batmobile"
a = re.compile(r"Bat(wo)?man")
print(a.search(s))
print(a.search(s1))

num1 = "The number 654-123-4567 is my US number"
num2 = "The number 456-9823 is my local number"

b = re.compile(r"\d\d\d(-\d\d\d)?-\d\d\d\d")
print(b.search(num1))
print(b.search(num2))

str1 = "The Batwoman is more powerful than Batman"
str2 = "The Batwowowoman is more powerful than batwoman"
str3 = "The Batman is more powerful than Batwowoman"
hero = re.compile(r"Bat(wo)*man")

print(hero.search(str1))
print(hero.search(str2))
print(hero.search(str3))

p = "I laughed out HaHaHa in the party"
p1 = "I laughed out HaHaHaHa in the party"
p2 = "I laughed out HaHaHaHaHa in the party"
c = re.compile(r'(Ha){3,5}')  #Greedy RegEx
d = re.compile(r'(Ha){3,5}?') #Non Greedy Regex
print(c.search(p))
print(c.search(p1))
print(c.search(p2))

print(d.search(p))
print(d.search(p1))
print(d.search(p2))

string = "Cell: 415-555-9856 Work: 546-654-6534"
phoneno = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneno1 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneno.findall(string))
print(phoneno1.findall(string))
x = phoneno.finditer(string)
for i in x:
    print(i.group())


s = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves'

words = re.compile(r'\d(\d)?\s\w(\w){3,8}')

words1 = re.compile(r'\d+\s\w+')

kk = words.finditer(s)
kk1 = kk = words1.finditer(s)
for i in kk:
    print(i.group())

for j in kk1:
    print(j.group())


l = "Everyone should eat good food"
m = "my version is 4.0 and counting."
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex1 = re.compile(r'[A-Z0-9]')
vowel_regex2 = re.compile(r'[0-5.]')
vowel_regex3 = re.compile(r'[^aeiouAEIOU]')
print(vowel_regex.findall(l))
print(vowel_regex1.findall(l))
print(vowel_regex2.findall(m))
print(vowel_regex3.findall(m))


o = "Hello are we good?"
startRegEx = re.compile(r'^Hell')   # string starts with something is carot
print(startRegEx.findall(o))

startRegEx1 = re.compile(r'ood?$')  # string ends with something is dollar  -  since ? is not escaped it is null
print(startRegEx1.findall(o))

startRegEx2 = re.compile(r'good\?$')
print(startRegEx2.findall(o))

text = input("Write a string: ")
regex = re.compile(r'\d$')
m = regex.search(text)
if(m != None):
    print("It ends with a digit ")
else:
    print("It dosen't end with a digit")

char = "The fat cat sat on the mat and wore a hat"
startRegEx = re.compile(r'.at')         #match any preceeding character
print(startRegEx.findall(char))
startRegEx1 = re.compile(r'.*at')       #match any and all characters
print(startRegEx1.findall(char))

s = "<To serve a man> for dinner"
regex = re.compile(r'<.*>')
print(regex.search(s))


s = "Serve the public trust. Protect the innocents"
reg = re.compile(r'.*',re.DOTALL)
print(reg.findall(s))

s = "Robocop got the bike from ROBOCOP"
startRegEx = re.compile(r'robocop',re.IGNORECASE)
print(startRegEx.findall(s))

str = "Agent Alice gave the secret documents to Agent Bob."
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub('CENCORED',str))