def day13a_mod():
    f = open('input\\input13.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    firewalls = {}
    for line in lines:
        data = line.split(':')
        depth = int(data[0])
        rng = int(data[1])
        firewalls[depth] = rng
    
    severity = 0
    for layer in sorted(list(firewalls.keys())):
        rng = firewalls[layer]
        if layer % (2*(rng-1)) == 0:
            severity += layer*rng
            
    return severity
    
print(day13a_mod())