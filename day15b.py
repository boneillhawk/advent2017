import itertools
import functools
import copy
import collections
import heapq
import math
import hashlib

def day15b():
    a = 516 #input
    b = 190
    mod = 2147483647
    count = 0
    for i in range(5000000):
        a = (a * 16807) % mod
        while a%4 != 0:
            a = (a * 16807) % mod
        b = (b * 48271) % mod
        while b%8 != 0:
            b = (b * 48271) % mod
        a_str = bin(a)[2:]
        b_str = bin(b)[2:]
        while len(a_str) < 16:
            a_str = '0'+a_str
        while len(b_str) < 16:
            b_str = '0'+b_str

        count += (1 if a_str[-16:] == b_str[-16:] else 0)
    
    return count
    
print(day15b())