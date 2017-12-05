import itertools
import copy
import collections
import heapq
import math
import hashlib

def day5a():
    f = open('input\\input5.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    jumps = [int(x) for x in lines]
    
    i = 0
    counter = 0
    exit = len(jumps)
    
    while i < exit:
        jumps[i] += 1
        i += (jumps[i] - 1)
        counter += 1
        
    return counter

print(day5a())