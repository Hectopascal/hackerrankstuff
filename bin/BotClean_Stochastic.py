#!/usr/bin/python
def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print "CLEAN"
        return
    for y in range (0,5):
        for x in range (0,5):
            if board[y][x] == 'd' :
                break
        if board[y][x] == 'd' :
                break
    if y > posr :
        next = "DOWN"
    elif y < posr :
        next = "UP"
    elif x > posc :
        next = "RIGHT"
    elif x < posc :
        next = "LEFT"
    print next
    return

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
