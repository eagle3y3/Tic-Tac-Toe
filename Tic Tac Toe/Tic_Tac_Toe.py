'''
Created on Dec 1, 2018

@author: Lester H

Tic Tac Toe 
'''
import random

def drawBoard(board):
    #function for printing board
    # "board is a list of 10 strings" (ignore index 0)
    print(' | |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' | |')
    print('-----------')
    print(' | |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' | |')
    print('-----------')
    print(' | |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' | |')

    
def inputPlayerLetter():
    #Gives player choice of letter x or o
    #Returns list with player's letter as the first item, and computer as the second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']

def whoGoesFirst():
    #randomly chooses who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #Function returns True if player wants to play again. Otherwise returns false/
    print ('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    # bo and le short for board and letter
    # Given board and player's letter, this function returns True if player won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #horizontal
            (bo[4] == le and bo[5] == le and bo[6] == le) or 
            (bo[1] == le and bo[2] == le and bo[3] == le) or 
            
            (bo[7] == le and bo[4] == le and bo[1] == le) or #vertical
            (bo[8] == le and bo[5] == le and bo[2] == le) or 
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            
            (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal 
            (bo[1] == le and bo[5] == le and bo[9] == le))

def getBoardCopy(board):
    # Make duplicate board of the board list and return to duplicate
    duplBoard = []
    
    for i in board:
        duplBoard.append(i)
        
    return duplBoard

def isSpaceFree(board, move):
    #return true if the passed move is blank
    return board[move] == ' '

def getPlayerMove(board):
    #let player type in move
    move = ' '
    
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    #returns a valid move from the passed list on the passed board
    #returns None if there is no valid move
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #Given a board and computer's letter, determine where to move and return move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #check if win in the next move
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #computer takes corners if possible
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    #computer tries to take center if possible
    if isSpaceFree(board, 5):
        return 5
    # return sides 
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #Return True if every space of the board has been taken otherwise return False
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    #reset board
    theBoard = [' ']* 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The' + turn + 'will go first')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congrats you won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
                
            
        
        

        
        

