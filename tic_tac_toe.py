import random    

theBoard = {'1': ' ', '2': ' ', '3': ' ',
'4': ' ', '5': ' ', '6': ' ',
'7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
       
   
for i in range(1,10,1):
    printBoard(theBoard)
    
    if i%2 != 0:
        print("\tPERSON-1 TURN \n")
        move1 = input("ENTERED MOVE :>" )
        turn1 ='X'
        theBoard[move1] = turn1
    else:
        print("\t PERSON-2 TURN\n")
        move2 = input("ENTERED MOVE :>" )
        turn2 ='O'
        theBoard[move2] = turn2

    
