#continue and break

while(True):
    name = input("Username: ")
    if(name=="Joey"):
        break
    else:
        print("Invalid username")
        continue
while(True):
    password = input("Password:")
    if(password=="testme"):
        break
    else:
        print("Invalid password")
        continue
print("\n\n\n\t\t\tYou have successfully logged in.....")