# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
#  https://www.geeksforgeeks.org/javascript-function-parameters/ 
# A note on style: Dictionaries can be defined before or after functions.
#Claryse


import sys
board = {'TL':' ', 'TM':' ', 'TR':' ', 'ML':' ', 'MM':' ', 'MR':' ', 'BL':' ', 'BM':' ', 'BR':' '}

def TTT (board):
    print(" %s | %s | %s"%(board['TL'],board['TM'], board['TR']))
    print("---+---+---")
    print(" %s | %s | %s"%(board['ML'], board['MM'], board['MR']))
    print("---+---+---")
    print(" %s | %s | %s "%(board['BL'], board['BM'], board['BR']))

def checkwin(board):
    if board['TL'] == board['TM'] == board['TR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['TL'] == board['TM'] == board['TR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['ML'] == board['MM'] == board['MR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['ML'] == board['MM'] == board['MR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['BL'] == board['BM'] == board['BR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['BL'] == board['BM'] == board['BR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['TL'] == board['ML'] == board['BL'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['TL'] == board['ML'] == board['BL'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['TM'] == board['MM'] == board['BM'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['TM'] == board['MM'] == board['BM'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['TR'] == board['MR'] == board['BR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['BL'] == board['BM'] == board['BR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['BL'] == board['MM'] == board['TR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['BL'] == board['MM'] == board['TR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif board['TL'] == board['MM'] == board['BR'] == 'O':
        print("Congragulations! O won!")
        return True
    elif board['TL'] == board['MM'] == board['BR'] == 'X':
        print("Congragulations! X won!")
        return True
    elif RRR(board):
        return True
    else:
        return False

print("Hi! Welcome to Tic Tac Toe! Pick Who is X's and who is O's!")
print("You can exit the game at any time by printing 'exit'.")
print("Type in the first two capital letters of your choice. So, if you pick the bottom right square, type 'BR'.")
TTT(board)
def RRR (board):
    for key in board: 
        if board[key] == ' ':
            return False
    return True

while True:
    carrot = input("Player X! Pick a square!: ")
    if carrot == 'exit':
        sys.exit()
    while carrot not in board.keys():
        carrot = input("Oops! Try again!")
        if carrot == 'exit':
            sys.exit()
    while board[carrot] != ' ':
        carrot = input("Sorry! That space is full! Choose again")
    board[carrot] = 'X'
    TTT(board)

    if checkwin(board):
        break
    radish  = input("Player O! Pick a square!")
    if radish == 'exit':
        sys.exit()
    while radish not in board.keys():
        radish = input("Oops! Try again!")
        if radish == 'exit':
            sys.exit()
    while board[radish] != ' ':
        radish = input("Sorry! That space is full! Choose again")
    board[radish] = 'O'
    TTT(board)



