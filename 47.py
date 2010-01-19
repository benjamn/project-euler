from util import *

def has_n_factors(x, n):
    return len(distinct_factors(x)) == n

def test(*args):
    l = len(args)
    return all(has_n_factors(x, l) for x in args)

stride = 4
for n in xrange(0, 1000000):
    if test(*range(n, n + stride)):
        print n, distinct_factors(n)
        print n+1, distinct_factors(n+1)
        print n+2, distinct_factors(n+2)
        print
