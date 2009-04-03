
def inc(p):
    next = str(int(''.join(str(d) for d in p)) + 1)
    if len(next) == 9:
        next = '0' + next
    return [int(c) for c in next]
    
def distinct(p):
    if len(p) != 10:
        return False
    for i in xrange(10):
        if i not in p:
            return False
    return True

def next(p):
    p = inc(p)
    while not distinct(p):
        p = inc(p)
    return p

perm = range(10)
for i in range(100):
    perm = next(perm)
    print perm, i

print perm