from tkinter import *
from functools import partial
from typing import DefaultDict
from random import seed
from random import random

global dict1
dict1 = {}
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

randSeed = 1

def chooseX():
    start.destroy()
    makeBoard("X", "O")

def chooseO():
    start.destroy()
    makeBoard("O", "X")

def startgame():
    global start
    start = Tk()
    start.geometry("250x250")
    start.title('Tic Tac Toe')
    l1 = Label(start, text="Choose X's or O's")
    l1.grid(row=0, column=0, columnspan=2)
    x = Button(start, text = "X", command=chooseX, width=7, bd=5)
    o = Button(start, text = "O", command=chooseO, width=7, bd=5)
    x.grid(row =1, column=0)
    o.grid(row=1, column=1)

    start.mainloop()

    

def makeBoard(p1, p2):
    global root
    root = Tk()
    root.geometry("250x250")
    root.title('Tic Tac Toe')
    for i in range(3):
        for j in range(3):
            get_comm = partial(playTurn, i, j, p1, p2)
            dict1[(i, j)] = Button(root, command=get_comm, text=" ", width=10, bd = 5)
            dict1[(i, j)].grid(row=i, column=j)
    
    if(p1 == 'O'):
        move = getMove(board, p1, p2)
        dict1[(move[0], move[1])].config(text = p2)
        board[move[0]][move[1]] = p2

    #root.title("Tic Tac Toe")
    root.mainloop()

def restart():
    root.destroy()
    board.clear()
    board.append([" ", " ", " "])
    board.append([" ", " ", " "])
    board.append([" ", " ", " "])
    startgame()

def reset(p1, p2):
    score = eval(board, p1, p2)
    if (score < 0):
        l2 = Label(root, text="You Win!")
        l2.grid(row=4,column=0, columnspan=3)
    elif (score > 0):
        l2 = Label(root, text="You Lose!")
        l2.grid(row=4,column=0, columnspan=3)
    else:
        l2 = Label(root, text="Tie!")
        l2.grid(row=4,column=0, columnspan=3)

    but = Button(root, text="Click to retry", command=restart)
    but.grid(row=5, column=0)
    

def playTurn(x, y, p1, p2):
    if(board[x][y] == " "):
        dict1[(x, y)].config(text = p1)
        board[x][y] = p1
        if (gameFinished(board, p1, p2)):
            reset(p1, p2)
            return
        move = getMove(board, p1, p2)
        dict1[(move[0], move[1])].config(text = p2)
        board[move[0]][move[1]] = p2
        if (gameFinished(board, p1, p2)):
            reset(p1, p2)
            return

    else:
        return

def eval(board, p1, p2):
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            if (board[i][0] == p2):
                return 10
            elif (board[i][0] == p1):
                return -10

    for j in range(3):
        if(board[0][j] == board[1][j] and board[1][j] == board[2][j]):
            if(board[0][j] == p2):
                return 10
            elif(board[0][j] == p1):
                return -10

    if(board[0][0] == board[1][1]  and board[1][1] == board[2][2]):
        if (board[0][0] == p2):
            return 10
        elif(board[0][0] == p1):
            return -10

    if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == p2):
            return 10
        elif(board[0][2] == p1):
            return -10


    return 0


def getScore(board, depth, isComputer, p1, p2):
    score = eval(board, p1 ,p2)
    filled = True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                filled = False
    
    if(filled):
        return depth + score
    
    if(score == 10 or score == -10):
        return depth + score
    
    else:
        if(isComputer):
            for i in range(3):
                for j in range(3):
                    if(board[i][j] == ' '):
                        board[i][j] = p2

                        score = max(score, depth + getScore(board, depth + 1, False, p1, p2))
                                       
                        board[i][j] = ' '
            return score
        
        else:
            for i in range(3):
                for j in range(3):
                    if(board[i][j] == ' '):
                        board[i][j] = p1

                        score = min(score, depth + getScore(board, depth + 1, True, p1, p2))

                        board[i][j] = ' '
            return score



def getMove(board, p1, p2):
    score = -9999
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                board[i][j] = p2

                newScore = getScore(board, 0, False, p1, p2)

                if(newScore > score):
                    move = (i, j)
                    score = newScore

                board[i][j] = ' '


    return move

def gameFinished(board, p1, p2):
    filled = True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                filled = False
    if (eval(board, p1, p2) != 0):
        return True
    
    return filled

startgame()

