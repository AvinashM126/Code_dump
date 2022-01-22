# Tic Tac Toe

tictac = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
player = 1
count = 0
def print_board():
    print("\nBOARD\n")
    for i in tictac:
        if(i == 1 or i == 4 or i == 7):
            print("\n")
        print(tictac[i],'   ',end = " ")

def getwinner():
    if((tictac[1] == tictac[2] == tictac [3])or(tictac[4] == tictac[5] == tictac[6])or(tictac[7] == tictac[8] == tictac[9])or(tictac[1] == tictac[4] == tictac[7])or(tictac[2] == tictac[5] == tictac[8])or(tictac[3] == tictac[6] == tictac[9])or(tictac[1] == tictac[5] == tictac[9])or(tictac[3] == tictac[5] == tictac[7])):
        return True
    else:
        return False

print_board()
while(count<9):
    count+=1
    getinput()
    ret=check()
    if(ret == True):
        continue
    else:
        getinput()
    if(player == 1):
        tictac[pos] = 'X'
        print(tictac)
    elif(player == 2):
        tictac[pos] ='O'
    if(player == 1):
        player = 2
    elif(player == 2):
        player = 1
    print_board()
    if(getwinner()==False):
        continue
    else:
        break

if(player == 1):
        player = 2
elif(player == 2):
        player = 1
if(count<9):
    print("\n\n\t\tThe Winner is \"Player ",player,"\"")
else:
    print("\n\n\t\tThe match is a DRAW")

