#!/bin/python
import sys
import fileinput
import math

def displayPathtoPrincess(n,grid):
    x = 0
    y = 0
    i = (n-1)/2
    if grid[0][0] == 'p':
        #top left
        count = 0
        while count<i:
            count+=1
            print "UP"
            print "LEFT"
            
    elif grid[0][n-1]=='p':
        loc = 'tr'
        count = 0
        while count<i :
            count+=1
            print "UP"
            print "RIGHT"
            
    elif grid[n-1][0]=='p':
        loc = 'bl'
        count = 0
        while count<i :
            count+=1
            print "DOWN"
            print "LEFT"
            
    elif grid[n-1][n-1]=='p':
        loc = 'br'
        count = 0
        while count<i :
            count+=1
            print "DOWN"
            print "RIGHT"
            
    return
    
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
