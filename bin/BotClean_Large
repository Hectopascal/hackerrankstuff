#!/usr/bin/python
#For BotCLean Large on HackerRank
#final score 54.2

import math
from functools import partial
list = []
def next_move(posr, posc, dimh, dimw, board):
    if board[posr][posc] == 'd':
        print "CLEAN"
        return
    for y in range (0,dimh):
        for x in range (0,dimw):
            if board[y][x] == 'd' :
                if [x,y] not in list :
                    list.append([x,y])
                
    tomove = closest_node([posc,posr],list)
    if tomove[1] > posr :
        next = "DOWN"
    elif tomove[1] < posr :
        next = "UP"
    elif tomove[0] > posc :
        next = "RIGHT"
    elif tomove[0] < posc :
        next = "LEFT"
    print next
    return

def closest_node(node, coords):
    min = 71
    minIn = [0,0]
    for n in coords:
        dist = math.sqrt(math.pow(n[0]-node[0],2) + math.pow(n[1]-node[1],2))
        #pythygoras for distance between 2 points
        if dist < min :
            min = dist
            minIn = n

    return minIn

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
