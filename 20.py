# Fake password Manager
import sys,pyperclip

password = {'gmail':'gmail1234','facebook':'facebook12345','microsoft':'microsoft12345','pinrest':'pinrest12345','adobe':'adobe12345','soundcloud':'soundcloud12345','amazon':'amazon12345','flipkart':'flipkart12345','snapdeal':'snapdeal12345','uber':'uber12345','ola':'ola12345','irctc':'irctc12345','ksrtc':'ksrtc12345'}

if sys.argv[1] in password:
    pyperclip.copy(password[sys.argv[1]])