import itertools
import copy
import collections
import heapq
import math
import hashlib

def day9a():
    f = open('input\\input9.txt', 'r')
    data = [line.strip() for line in f.readlines()][0]
    f.close()

    depth = 0
    index = 0
    total = 0
    while index < len(data):
        ch = data[index]
        if ch == '{':
            depth += 1
            total += depth
            index += 1
        elif ch == '}':
            depth -= 1
            index += 1
        elif ch == '<':
            index += 1
            while data[index] != '>':
                if data[index] == '!':
                    index += 2
                else:
                    index += 1
            index += 1
        else:
            index += 1
        
    return total
        
    
print(day9a())