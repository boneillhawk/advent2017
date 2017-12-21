from knot_hash import knot_hash

def day14b(data):
    used_spaces = set()
    for i in range(128):
        row = data + '-' + str(i)
        hash = knot_hash(row)
        bin_string = bin(int(hash, 16))[2:]
        while len(bin_string) < 128:
            bin_string = '0'+bin_string
        for ch in range(len(bin_string)):
            if bin_string[ch] == '1':
                used_spaces.add( (i,ch) )
                
    regions = 0
    while used_spaces:
        first = used_spaces.pop() # Start with an arbitrary elt by removing it...
        used_spaces.add(first) #... but put it back!
        fringe = [first]
        visited = set()
        in_region = set()
        while fringe:
            current = fringe.pop()
            visited.add(current)
            if current in used_spaces:
                in_region.add(current)
                for n in neighbors(current):
                    if n not in visited and n not in fringe and n not in in_region and n in used_spaces:
                        fringe.append(n)
            
        used_spaces -= in_region
        #print(len(in_region))
        regions += 1
        
    return regions
    
def neighbors(coords):
    x,y = coords
    neighbors = []
    if x-1 >= 0:
        neighbors.append((x-1,y))
    if x+1 < 128:
        neighbors.append((x+1,y))
    if y-1 >= 0:
        neighbors.append((x,y-1))
    if y+1 < 128:
        neighbors.append((x,y+1))
    
    return neighbors
            
print(day14b('flqrgnkx'))
print(day14b('uugsqrei'))
