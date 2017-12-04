import itertools
import copy
import collections
import heapq
import math
import hashlib

def day4b():
    f = open('input\\input4.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    total = 0
    for line in lines:
        passwords = line.split()
        #sorted_words = [''.join(sorted(wl)) for wl in [list(x) for x in passwords]]
        sorted_words = []
        for word in passwords:
            wordlist = list(word)
            sorted_words.append(''.join(sorted(wordlist)))
        pass_set = set(sorted_words)
        if len(passwords) == len(pass_set):
            total += 1
            
    return total
    
print(day4b())