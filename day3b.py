import itertools
import copy
import collections
import heapq
import math
import hashlib

def day3b():
    data = 265149
    value = 1
    matrix = [[1]]
    expand(matrix)
    counter = 1
    coords = [1,1]
    direction = 'R'
    while value<data:
        counter += 1
        if counter == 23:
            print(matrix)
        if direction == 'R':
            coords[1] += 1
            if coords[0] == len(matrix)-1 and coords[1] >= len(matrix)-1:
                expand(matrix)
                coords[0]+=1
                coords[1]+=1
            elif coords[1] >= len(matrix)-1:
                direction = 'U'
        elif direction == 'L':
            coords[1] -= 1
            if coords[1] == 0:
                direction = 'D'
        elif direction == 'U':
            coords[0] -= 1
            if coords[0] == 0:
                direction = 'L'
        elif direction == 'D':
            coords[0] += 1
            if coords[0] == len(matrix)-1:
                direction = 'R'
        print(coords, direction)
        value = calcsum(matrix, coords[0], coords[1])
        print(value)
        matrix[coords[0]][coords[1]] = value
    return value
        
def calcsum(matrix, x, y):
    total = 0
    if x>=1 and y >= 1:
        total += matrix[x-1][y-1]
    if x>=1:
        total += matrix[x-1][y]
    if x>=1 and y<len(matrix)-1:
        total += matrix[x-1][y+1]
    if y >= 1:
        total += matrix[x][y-1]
    if y<len(matrix)-1:
        total += matrix[x][y+1]
    if x<len(matrix)-1 and y>=1:
        total += matrix[x+1][y-1]
    if x<len(matrix)-1:
        total += matrix[x+1][y]
    if x<len(matrix)-1 and y<len(matrix)-1:
        total += matrix[x+1][y+1]
    return total
    
def expand(matrix):
    matlen = len(matrix)
    matrix.insert(0,[0]*(matlen+2))
    matrix.append([0]*(matlen+2))
    for row in range(1,matlen+1):
        matrix[row].insert(0,0)
        matrix[row].append(0)
    
    
print(day3b())