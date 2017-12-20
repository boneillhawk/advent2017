import itertools
import functools
import copy
import collections
import heapq
import math
import hashlib

def day12b():
    f = open('input\\input12.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    graph = {}
    all_nodes = set()
    for line in lines:
        data = line.split()
        id = int(data[0])
        nodes = []
        for k in data[2:]:
            x = int(k.strip(','))
            nodes.append(x)
        graph[id] = tuple(nodes)
        all_nodes.add(id)
    
    groups = 0
    while all_nodes:
        groups += 1
        visited = set()
        fringe = collections.deque()
        fringe.append(min(all_nodes))
        while fringe:
            current = fringe.popleft()
            succ = graph[current]
            visited.add(current)
            for n in succ:
                if n not in visited and n not in fringe:
                    fringe.append(n)
        all_nodes -= visited
        
    return groups
    
print(day12b())