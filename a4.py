# "R" represents user one; "B" represents user two; "*" represents an empty space
# the board is represented by a 11 by 11 square grid
import math
def initialize():
    board=[]
    for i in range(0,11):
        board.append([])
    for i in range(0,11):
        for j in range(0,11):
            board[i].append('*')
    return board
        
def switch_player(current):
    if current==1:
        return 2
    else:
        return 1

def change_board(board,player,position): # position is input as a list of two integers
    if player==1:
        board[position[0]][position[1]]='R'
    else:
        board[position[0]][position[1]]='B'
    return 

def left_connect(board,a,x,y):
    if y<0 or y>10 or board[x][y]!=a:
        return False
    else:
        if x==0:
            return True
        else:
            return left_connect(board,a,x-1,y-1) or left_connect(board,a,x-1,y) or left_connect(board,a,x-1,y+1)
        
def right_connect(board,a,x,y):
    if y<0 or y>10 or board[x][y]!=a:
        return False
    else:
        if x==10:
            return True
        else:
            return right_connect(board,a,x+1,y-1) or right_connect(board,a,x+1,y) or right_connect(board,a,x+1,y+1)

def up_connect(board,a,x,y):
    if x<0 or x>10 or board[x][y]!=a:
        return False
    else:
        if y==0:
            return True
        else:
            return up_connect(board,a,x-1,y-1) or up_connect(board,a,x,y-1) or up_connect(board,a,x+1,y-1)

def down_connect(board,a,x,y):
    if x<0 or x>10 or board[x][y]!=a:
        return False
    else:
        if y==10:
            return True
        else:
            return down_connect(board,a,x-1,y+1) or down_connect(board,a,x,y+1) or down_connect(board,a,x+1,y+1)
    
def check_status(board,player,x,y): # decide by recursion whether one party has won
    if player==1:
        a='R'
    else:
        a='B'
    if left_connect(board,a,x,y) and right_connect(board,a,x,y):
        return True
    elif up_connect(board,a,x,y) and down_connect(board,a,x,y):
        return True
    else:
        return False

def get_position(board):
    while (1):
        x=input('enter an integer as x coordinate between 0 and 10 seperated by a space')
        y=input('enter an integer as y coordinate between 0 and 10 seperated by a space')
        if int(x)>=0 and int(x)<=10 and int(y)>=0 and int(y)<=10 and board[int(x)][int(y)]=='*':
            return [int(x),int(y)]
        else:
            print('invalid input, try again')

def print_board(board):
    for i in range(0,11):
        print(board[i])
    return 

def main():
    board=initialize()
    player=1
    over=False
    while not over:
        pos=get_position(board)
        change_board(board,player,pos)
        print_board(board)
        over=check_status(board,player,pos[0],pos[1])
        player=switch_player(player)
    print('game is over. player %d wins',(player+1)%2)
        
main()