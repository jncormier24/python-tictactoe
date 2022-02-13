winner = False
player1 = 'X'
player2 = 'O'
currentplayer = 1
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
numpadrow1 = [7,8,9]
numpadrow2 = [4,5,6]
numpadrow3 = [1,2,3]

def showgameboard(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    
def shownumpad():
    showgameboard(numpadrow1, numpadrow2, numpadrow3)

def checkwinner(row1, row2, row3):
    # across row 1
    if row1[0] == currentplayer and row1[1] == currentplayer and row1[2] == currentplayer:
        return currentplayer
    # across row 2
    elif row2[0] == currentplayer and row2[1] == currentplayer and row2[2] == currentplayer:
        return currentplayer
    # across row 3
    elif row3[0] == currentplayer and row3[1] == currentplayer and row3[2] == currentplayer:
        return currentplayer
    # down column 1
    elif row1[0] == currentplayer and row2[0] == currentplayer and row3[0] == currentplayer:
        return currentplayer
    # down column 2
    elif row1[1] == currentplayer and row2[1] == currentplayer and row3[1] == currentplayer:
        return currentplayer
    # down column 3
    elif row1[2] == currentplayer and row2[2] == currentplayer and row3[2] == currentplayer:
        return currentplayer
    # diagonal top to bottom
    elif row1[0] == currentplayer and row2[1] == currentplayer and row3[2] == currentplayer:
        return currentplayer
    # diagonal bottom to top
    elif row1[2] == currentplayer and row2[1] == currentplayer and row3[0] == currentplayer:
        return currentplayer
    else:
        return False

def switchplayer(currentplayer):
    if currentplayer == 1:
        currentplayer = 2
    else:
        currentplayer = 1
        
def getValidPlayerInput():
    playerinput = input("Player {}, where would you like to put your piece? ".format(currentplayer))
    
    if playerinput not in range(1, 10):
        print("Please enter valid input. Try again.")
        getValidPlayerInput()

    if playerinput in range(7, 10):
        if row1[playerinput - 7] == '':
            row1[playerinput - 7] = currentplayer
        else:
            getValidPlayerInput()
    elif playerinput in range(4, 7):
        if row2[playerinput - 4] == '':
            row2[playerinput - 4] = currentplayer
        else:
            getValidPlayerInput()
    else:
        if row3[playerinput] == '':
            row3[playerinput] = currentplayer
        else:
            getValidPlayerInput()
        

while winner == False:
    shownumpad()
    getValidPlayerInput()
    
    winner = checkwinner(row1, row2, row3)
    if winner == False:
        switchplayer(currentplayer)
        
print("The winner is {}".format(currentplayer))