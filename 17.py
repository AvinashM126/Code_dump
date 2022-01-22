text = input("Enter the text: ")
count = {}
for i in text:
    count[i] = count.get(i,0) + 1
print("Text: ",text,"\n","Text count",count)