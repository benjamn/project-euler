from util import is_prime
    
def run(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

mx = 0
for a in xrange(-999, 1000):
    print a
    for b in xrange(1000):
        r = run(a, b)
        if r > mx:
            mx = r
            print '***', r, a, b, a*b
