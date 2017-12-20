def day13b_mod():
    f = open('input\\input13.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    
    firewalls = {}
    for line in lines:
        data = line.split(':')
        depth = int(data[0])
        rng = int(data[1])
        firewalls[depth] = rng
    
    caught = True
    t=0
    while caught:
        caught = False
        for layer in sorted(list(firewalls.keys())):
            rng = firewalls[layer]
            if (layer+t) % (2*(rng-1)) == 0:
                caught = True
        if caught:
            t+= 1
    return t
    
print(day13b_mod())