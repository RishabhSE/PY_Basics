import random    

theBoard = {'1': ' ', '2': ' ', '3': ' ',
'4': ' ', '5': ' ', '6': ' ',
'7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
       
turn = 'X'
for i in range(1,10,1):
    printBoard(theBoard)

    move = input("ENTER MOVE:>" )
    
    if turn == 'X':
        turn = 'O'
        theBoard[move] = turn 
    else:
        turn = 'X'
        theBoard[move] = turn 

       
        
  
