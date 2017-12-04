import itertools
import copy
import collections
import heapq
import math
import hashlib

def day2():
	f = open('input\\input2.txt', 'r')
	lines = [line.strip() for line in f.readlines()]
	f.close()

	total = 0
	for line in lines:
		data = [int(x) for x in line.split()]
		diff = max(data) - min(data)
		total += diff
		
	return total
	
	
print(day2())