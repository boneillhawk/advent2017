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
		for i in range(len(data)):
			for j in range(i+1,len(data)):
				if i == j:
					continue
				elif data[i]%data[j] == 0:
					total += data[i]//data[j]
				elif data[j]%data[i] == 0:
					total += data[j]//data[i]
		
	return total
	
	
print(day2())