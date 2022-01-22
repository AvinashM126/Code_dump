# Shelf

import shelve

ct = ['city1','city2','city3']
st = ['state1','state2','state3']

shelfFile = shelve.open("ShelfFile.txt")

shelfFile['cities'] = ct
shelfFile['states'] = st

shelfFile.close()

shelfFile = shelve.open("ShelfFile.txt")
print(shelfFile['cities'])
print(shelfFile['states'])

shelfFile.close()

shelfFile = shelve.open("ShelfFile.txt")
print(list(shelfFile.keys()))
shelfFile.close()

