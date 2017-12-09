import itertools
import copy
import collections
import heapq
import math
import hashlib

def day8():
    f = open('input\\input8.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    max_seen = 0
    registers = {}
    for line in lines:
        data = line.split()
        reg = data[0]
        mult = 1 if data[1] == 'inc' else -1
        amount = int(data[2])
        if_reg = data[4]
        op = data[5]
        if_amt = int(data[6])
        
        if compare(registers, if_reg, op, if_amt):
            value = registers.get(reg, 0)
            registers[reg] = value+(mult*amount)
            max_seen = max(max_seen, registers[reg])
            
    return max(registers.values()), max_seen
    
def compare(registers, reg, op, amt):
    ops = {'<':int.__lt__, '>':int.__gt__,
           '<=':int.__le__, '>=':int.__ge__,
           '!=':int.__ne__, '==':int.__eq__}
    value = registers.get(reg, 0)
    return ops[op](value,amt)
       
print(day8())