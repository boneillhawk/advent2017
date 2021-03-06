import itertools
import copy
import collections
import heapq
import math
import hashlib

def day6a():
    f = open('input\\input6.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    banks = [int(x) for x in lines[0].split()]
    
    observed = set()
    counter = 0
    while tuple(banks) not in observed:
        observed.add(tuple(banks))
        counter += 1
        
        index = -1
        for idx in range(len(banks)):
            if banks[idx] == max(banks):
                index = idx
                break
        
        distrib = banks[index]
        banks[index] = 0
        
        while distrib>0:
            index = (index+1)%len(banks)
            banks[index]+=1
            distrib-=1
    
    return counter
    
print(day6a())