import itertools
import copy
import collections
import heapq
import math
import hashlib

def day8a():
    f = open('input\\input8.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    registers = {}
    for line in lines:
        data = line.split()
        reg = data[0]
        mult = 1 if data[1] == 'inc' else -1
        amount = int(data[2])
        if_reg = data[4]
        arg = data[5]
        if_amt = int(data[6])
        
        result = evaluate(registers, if_reg, arg, if_amt)
        if result:
            value = registers.get(reg, 0)
            registers[reg] = value+(mult*amount)
            
    return max(registers.values())
    
def evaluate(registers, reg, arg, amt):
    value = registers.get(reg, 0)
    if arg == '<':
        return value < amt
    elif arg == '>':
        return value > amt
    elif arg == '<=':
        return value <= amt
    elif arg == '>=':
        return value >= amt
    elif arg == '==':
        return value == amt
    elif arg == '!=':
        return value != amt
    
print(day8a())