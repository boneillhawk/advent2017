import itertools
import copy
import collections
import heapq
import math
import hashlib

def day3():
    data = 265149
    
    root = int(math.sqrt(data))
    loc = [root//2,-(root//2)]
    value = root**2+1
    height = -loc[1] + 1
    
    while value < data and loc[1]<height:
        loc[1] += 1
        value += 1
    while value < data and loc[0]>-height:
        loc[0] -= 1
        value += 1
    while value < data and loc[1]>-height:
        loc[1] -= 1
        value += 1
    while value < data and loc[0]<height:
        loc[0] += 1
        value += 1
    print(loc)
    print(abs(loc[0])+abs(loc[1]))
    
print(day3())