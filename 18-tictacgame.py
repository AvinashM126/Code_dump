#tictac game

game = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}

def board(game):
    for i in game:
        print(game[i],"|",end = " ")
        if(int(i)%3 == 0):
            print("\n__  __  __""\n")

def findWinner():
    if(game['1']==game['2']==game['3']=='X'or game['1']==game['4']==game['7']=='X'or game['7']==game['8']==game['9']=='X'or game['1']==game['5']==game['9']=='X'or game['3']==game['6']==game['9']=='X'or game['2']==game['5']==game['8']=='X'or game['4']==game['5']==game['6']=='X'or game['3']==game['5']==game['7']=='X'):
        print("Player1 (X) is Winner")
        board(game)
        return True
    elif(game['1']==game['2']==game['3']=='O'or game['1']==game['4']==game['7']=='O'or game['7']==game['8']==game['9']=='O'or game['1']==game['5']==game['9']=='O'or game['3']==game['6']== game['9']=='O'or game['2']==game['5']==game['8']=='O'or game['4']==game['5']==game['6']=='O'or game['3']==game['5']==game['7']=='O'):
        print("Player2 (O) is Winner")
        board(game)
        return True

def startthegame(player, game):

    chance = player

    for i in range(9):
        board(game)
        print("It's", chance ,"turn")
        while True:
            position = input("for which position:")
            if(game[position] == 'X' or game[position] == 'O'):
                print("The Position is already filled. Please enter Different Position")
            else:
                break
        game[position] = chance
        if(chance == player1):
            chance = player2
        else:
            chance = player1
        if findWinner():
            flag = 1
            break
    if flag == 1:
        print("Thank You")
    else:
        print("Match is draw")

print("\n\n\t\t\t\tLet's Play Tic Tac game\t\t\t\t\n")
print("player 1 is X\nPlayer 2 is O\n")
player1 = 'X'
player2 = 'O'
print("Let's Start the Game")
board(game)
print("Who wants to start the game? player1 or player2:\nEnter X or O:")
while True:
    player = input()
    if (player == 'X'):
        startthegame(player,game)
    elif (player == 'O'):
        startthegame(player,game)
    else:
        print("Please Enter X or O")
        continue