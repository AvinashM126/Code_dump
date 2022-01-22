import calci
print("\n\n\t\t\t\"Calculator\"\n\n")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Select any of the following operation:\n1.  Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
choice=input()
if(choice=="Addition"):
    print("\nSum:",calci.add(a,b)) 
elif(choice=="Subtraction"):
    print("\nDiifference: ",calci.sub(a,b))
elif(choice=="Multiplication"):
    print("\nProduct:",calci.mul(a,b))
elif(choice=="Division"):
    print("\nQuotient:",calci.div)