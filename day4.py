import itertools
import copy
import collections
import heapq
import math
import hashlib

def day4a():
    f = open('input\\input4.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    total = 0
    for line in lines:
        passwords = line.split()
        pass_set = set(passwords)
        if len(passwords) == len(pass_set):
            total += 1
            
    return total
    
print(day4a())