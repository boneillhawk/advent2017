#3830345 -- too high, off by one -- SOLVED
def day13b():
    f = open('input\\input13.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    firewalls = {}
    scanners = {}
    directions = {}
    for line in lines:
        data = line.split(':')
        depth = int(data[0])
        rng = int(data[1])
        firewalls[depth] = rng
        scanners[depth] = 0
        directions[depth] = 1
        last = depth
        
    caught = True
    t=0
    last_start_point = (scanners.copy(), directions.copy())
    while caught:
        if t%100000==0: print(t)
        caught = False
        
        # Reset scanners/directions
        if t > 0:
            scanners = last_start_point[0]
            directions = last_start_point[1]
            advance_scanners(scanners, directions, firewalls)
            last_start_point = (scanners.copy(), directions.copy())
        
        current_layer = 0
        while current_layer <= last and not caught:
            if scanners.get(current_layer, -1) == 0:
                caught = True
            else:
                advance_scanners(scanners, directions, firewalls)
                #if t==10:
                    #print(t+current_layer, scanners)
            current_layer += 1
        if caught:
            t += 1
            
    return t
    
def advance_scanners(scanners, directions, firewalls):
    for layer in scanners:
        if scanners[layer] + directions[layer] < 0 or scanners[layer]+directions[layer] >= firewalls[layer]:
            directions[layer] *= -1
        scanners[layer] += directions[layer]
    
print(day13b())