#Dictionaries


allguests = {'Alice':{'apples':5,'pretzels':12},'Bob':{'ham sandwitches':3,'apples':2},'Carol':{'cups':3,'apple pies':1}}

count = {}
guest = {}

for guest in allguests.values():
    for items in guest.keys():
            print(guest)
            print(items)
            count[items] = count.get(items,0) + guest[items]
            print(count)