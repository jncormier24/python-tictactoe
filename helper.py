player1 = 'X'
player2 = 'O'
currentplayer = player1

def switchplayer(currentplayer):
    print(currentplayer, player1, player2)
    if currentplayer == player1:
        currentplayer = player2
    else:
        currentplayer = player1
    
    return currentplayer

currentplayer = switchplayer(currentplayer)
print(currentplayer)
currentplayer = switchplayer(currentplayer)
print(currentplayer)
currentplayer = switchplayer(currentplayer)
print(currentplayer)