import itertools
import copy
import collections
import heapq
import math
import hashlib

def day7a():
    f = open('input\\input7.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    candidates = set()
    for line in lines:
        parts = line.split()
        name = parts[0]
        candidates.add(name)
    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            for p in parts[3:]:
                p = p.rstrip(',')
                candidates.remove(p)
    return candidates
    
print(day7a())