def spiral(side):
    swne, nwse, n, inc = [1], [1], 1, 2
    while True:
        nwse.append(n + inc * 1)
        swne.append(n + inc * 2)
        nwse.append(n + inc * 3)
        swne.append(n + inc * 4)
        n += inc * 4
        inc += 2
    
        if len(nwse) == side and len(swne) == side:
            return sum(nwse) + sum(swne) - 1

print spiral(1001)