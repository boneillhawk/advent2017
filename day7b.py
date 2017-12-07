import itertools
import copy
import collections
import heapq
import math
import hashlib

def day7b():
    f = open('input\\input7.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    tree = dict()
    local_weights = dict()
    for line in lines:
        parts = line.split()
        parent = parts[0]
        weight = int(parts[1][1:-1])
        kids = ()
        if len(parts) >= 3:
            kids = tuple([p.rstrip(',') for p in parts[3:]])
        tree[parent] = kids
        local_weights[parent] = weight
    
    total_weights = local_weights.copy()
    
    verified = dict()
    for node in tree:
        verified[node] = False
    
    while not all(verified.values()):
        for parent,kids in tree.items():
            if not kids:
                verified[parent] = True
            elif all(verified[k] for k in kids) and not verified[parent]:
                kid_wgts = [total_weights[k] for k in kids]
                low = min(kid_wgts)
                high = max(kid_wgts)
                if low != high:
                    wrong, right = (low, high) if kid_wgts.count(low) == 1 else (high, low)
                    idx = kid_wgts.index(wrong)
                    diff = wrong - right
                    return kids[idx], local_weights[kids[idx]]-diff
                total_weights[parent] += sum(kid_wgts)
                verified[parent] = True
                
    return False
    
print(day7b())