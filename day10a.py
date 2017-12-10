import itertools
import copy
import collections
import heapq
import math
import hashlib

def day10a():
    f = open('input\\input10.txt', 'r')
    data = f.readline()
    f.close()
    
    lens = [int(x) for x in data.split(',')]
    
    mylist = list(range(256))
    current = 0
    skip = 0
    
    for i in lens:
        mylist = reverse(mylist, current, i)
        current += (i + skip)
        current = current%len(mylist)
        skip += 1
        
    return mylist[0]*mylist[1]

def reverse(mylist, start, amt):
    if start+amt > len(mylist):
        diff = (start+amt)-len(mylist)
        reversable = mylist[start:]+mylist[:diff]
        reversed = reversable[::-1]
        return reversed[-diff:]+mylist[diff:start]+reversed[:-diff]
    else:
        end = start+amt
        return mylist[:start]+mylist[end-1:start:-1]+[mylist[start]]+mylist[end:]
    
print(day10a())