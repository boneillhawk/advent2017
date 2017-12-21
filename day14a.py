from knot_hash import knot_hash

def day14a(data):
    used = 0
    for i in range(128):
        row = data + '-' + str(i)
        hash = knot_hash(row)
        bin_string = bin(int(hash, 16))[2:]
        used += bin_string.count('1')
    
    return used

print(day14a('flqrgnkx'))    
print(day14a('uugsqrei'))
