import math

# Broken
def day3a(data):
    root = int(math.sqrt(data))
    loc = [root//2,-(root//2)]
    value = root**2 + 1
    height = -loc[1] + 1
    
    while value < data and loc[1]<height:
        loc[1] += 1
        value += 1
    while value < data and loc[0]>-height:
        loc[0] -= 1
        value += 1
    while value < data and loc[1]>-height:
        loc[1] -= 1
        value += 1
    while value < data and loc[0]<height:
        loc[0] += 1
        value += 1
    #print(loc)
    return (abs(loc[0])+abs(loc[1]))
	
def day3a_v2(data):
    root = int(math.sqrt(data))
    if root % 2 == 0:
        root -= 1
    loc = [root//2,-(root//2)] # We're in the lower right corner of our grid.
    value = root**2
    max_xy = root//2 
    
    while value < data:
        # We need to expand the sprial now
        max_xy += 1
        
        # Let's take that next one step to the right to add root+1 to the spiral
        loc[0] += 1
        value += 1

        # From there we have to go up
        while value < data and loc[1]<max_xy:
            loc[1] += 1
            value += 1
        # Can't go up anymore, go left
        while value < data and loc[0]>-max_xy:
            loc[0] -= 1
            value += 1
        # Can't go left anymore, go down
        while value < data and loc[1]>-max_xy:
            loc[1] -= 1
            value += 1
        # Can't go down anymore, go right
        while value < data and loc[0]<max_xy:
            loc[0] += 1
            value += 1
        
        # Can't go right anymore. If we need to keep going, we need to loop back and expand.
    
    return abs(loc[0])+abs(loc[1])
	
def calcsum(matrix, x, y):
    total = 0
    if x>=1 and y >= 1:
        total += matrix[x-1][y-1]
    if x>=1:
        total += matrix[x-1][y]
    if x>=1 and y<len(matrix)-1:
        total += matrix[x-1][y+1]
    if y >= 1:
        total += matrix[x][y-1]
    if y<len(matrix)-1:
        total += matrix[x][y+1]
    if x<len(matrix)-1 and y>=1:
        total += matrix[x+1][y-1]
    if x<len(matrix)-1:
        total += matrix[x+1][y]
    if x<len(matrix)-1 and y<len(matrix)-1:
        total += matrix[x+1][y+1]
    return total
	
def expand(matrix):
    matlen = len(matrix)
    matrix.insert(0,[0]*(matlen+2))
    matrix.append([0]*(matlen+2))
    for row in range(1,matlen+1):
        matrix[row].insert(0,0)
        matrix[row].append(0)
		
def day3b(data):
    value = 1
    matrix = [[1]]
    expand(matrix)
    coords = [1,1]
    direction = 'R'
    
    while value<data:
        if direction == 'R':
            coords[0] += 1
            if coords[1] == len(matrix)-1 and coords[0] == len(matrix)-1:
                expand(matrix)
                coords[0]+=1
                coords[1]+=1
            elif coords[0] >= len(matrix)-1:
                direction = 'U'
        elif direction == 'L':
            coords[0] -= 1
            if coords[0] == 0:
                direction = 'D'
        elif direction == 'U':
            coords[1] -= 1
            if coords[1] == 0:
                direction = 'L'
        elif direction == 'D':
            coords[1] += 1
            if coords[1] == len(matrix)-1:
                direction = 'R'
        
        value = calcsum(matrix, coords[0], coords[1])
        
        matrix[coords[0]][coords[1]] = value
    return value