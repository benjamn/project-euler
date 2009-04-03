from util import divisors, memo, bound
from random import shuffle

@memo
def abundant(n):
    return sum(divisors(n)) > n
    
def abundants(l=0, u=28123):
    return (i for i in xrange(l, u+1) if abundant(i))

def notsum():
    total = 0
    for n in xrange(28123+1):
        for a in abundants(u=n):
            if abundant(n - a):
                break
        else:
            total += n
            print n, total
            yield n
            
print sum(notsum())
