from math import ceil

def get_dist(x,y):
    x,y = abs(x), abs(y)
    lower = min(x,y)
    if x == lower:
        return lower + (y-lower)//2
    else:
        return lower + (x-lower)

def day11(line):
    data = line.split(',')

    x = 0
    y = 0
    dists = []
    for move in data:
        if move == 'n':
            y += 2
        elif move == 's':
            y -= 2
        elif move == 'nw':
            x -= 1
            y += 1
        elif move == 'ne':
            x += 1
            y += 1
        elif move == 'sw':
            x -= 1
            y -= 1
        elif move == 'se':
            x += 1
            y -= 1
        dists.append(get_dist(x,y))
    
    #print(x,y)
    return get_dist(x,y), max(dists)    
    
f = open('input\\input11.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

print(day11('ne,ne,ne'))
print(day11('ne,ne,sw,sw'))
print(day11('ne,ne,s,s'))
print(day11('se,sw,se,sw,sw'))
print(day11('ne,ne,ne,n,sw'))
print(day11(lines[0]))