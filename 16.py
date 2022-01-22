#Dictionary
birthday = {"Alice":"April 1","Bob":"Dec 12","Carol":"Mar 4"}
name = input("\n\t\t\t\" DICTIONARY \"\n\nEnter your name: ")
if(name in birthday):
    print("Info:\tName: ",name,"\t B'day: ",birthday[name])
else:
    choice=input("\nNo such entry exists\nDo you want to make a new entry: ")
    if(choice == 'y'):
        birthday[name]=input("Enter the birthday: ")
        print("The data has been added.")

print(birthday)