from util import *

def pent(n):
    return n*(3*n-1)/2

def pents():
    i = 1
    while 1:
        yield pent(i)
        i += 1

lots = bound(pents(), 10000000)

pset = set(lots)

def diffs():
    for i in pset:
        for j in pset:
            if ((i+j) in pset and
                (i-j) in pset):
                yield i-j

print min(diffs())
