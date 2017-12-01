import itertools
import copy
import collections
import heapq
import math
import hashlib

f = open('input\\input1.txt', 'r')
line = f.readline().strip()
f.close()

total = 0
for idx in range(len(line)):
	if line[idx] == line[idx-1	]:
		total += int(line[idx])
		
print(total)