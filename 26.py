from util import bound

def expand(d):
    n = 1
    while True:
        digit = n / d
        yield digit
        if n % d == 0:
            break
        n -= digit * d
        n *= 10
        

def test_period(n, p):
    buf = []
    for i in expand(n):
        if len(buf) > 3*p:
            break
        buf.append(i)
        
    if len(buf) < p:
        return True
    
    buf.reverse()
    return buf[:p] == buf[p:2*p]

mx = 0
for n in xrange(1, 1000):
    p = 1
    while not test_period(n, p):
        p += 1
    if p > mx:
        mx = p
        print n, p
    else:
        print "(%s)" % n
