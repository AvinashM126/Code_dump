import random
entry = 'y'
print(random.randint(1,100))
for i in range(5):
    entry=input("\nDO you want to generate random no. again? ")
    if(entry == 'y'):
        print(random.randint(1,100))
        continue
    else:
        break
