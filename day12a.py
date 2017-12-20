import itertools
import functools
import copy
import collections
import heapq
import math
import hashlib

def day12a():
    f = open('input\\input12.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    graph = {}
    for line in lines:
        data = line.split()
        id = int(data[0])
        nodes = []
        for k in data[2:]:
            x = int(k.strip(','))
            nodes.append(x)
        graph[id] = tuple(nodes)
        
    visited = set()
    fringe = collections.deque()
    fringe.append(0)
    while fringe:
        current = fringe.popleft()
        succ = graph[current]
        visited.add(current)
        for n in succ:
            if n not in visited and n not in fringe:
                fringe.append(n)
        
    return len(visited)
    
print(day12a())