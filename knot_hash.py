"""A corrected version of Day 10, part b, necessary for Day 14"""

import functools

def knot_hash(data):
    lens = [ord(x) for x in data]
    lens += [17,31,73,47,23]
    
    mylist = list(range(256))
    current = 0
    skip = 0
    
    for rd in range(64):
        for i in lens:
            mylist = reverse(mylist, current, i)
            current += (i + skip)
            current = current%len(mylist)
            skip += 1

    dense = [xor(mylist,a,a+16) for a in range(0,len(mylist),16)]
    result = [hex(j)[2:] for j in dense]
    result = [result[i] if len(result[i]) == 2 else '0'+result[i] for i in range(len(result))]
    return ''.join(result)

def xor(mylist,start,end):
    return functools.reduce(lambda x, y: x^y, mylist[start:end])
    
def reverse(mylist, start, amt):
    if start+amt > len(mylist):
        diff = (start+amt)-len(mylist)
        reversable = mylist[start:]+mylist[:diff]
        reversed = reversable[::-1]
        return reversed[-diff:]+mylist[diff:start]+reversed[:-diff]
    else:
        end = start+amt
        return mylist[:start]+mylist[end-1:start:-1]+[mylist[start]]+mylist[end:]
