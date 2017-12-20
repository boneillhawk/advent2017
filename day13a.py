def day13a():
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
        
    severity = 0
    
    for i in range(last+1):
        if scanners.get(i, -1) == 0:
            severity += i*firewalls[i]
        for layer in scanners:
            if scanners[layer] + directions[layer] < 0 or scanners[layer]+directions[layer] >= firewalls[layer]:
                directions[layer] *= -1
            scanners[layer] += directions[layer]
            
    return severity
    
print(day13a())