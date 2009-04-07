from util import *

m = 55500

@memo
def hexa(n):
    return n*(2*n-1)
hexas = set(hexa(n) for n in range(m))

@memo
def pent(n):
    return n*(3*n-1)/2
pents = set(pent(n) for n in range(m))

@memo
def trig(n):
    return n*(n+1)/2
trigs = set(trig(n) for n in range(m))

print max(hexas.intersection(pents).intersection(trigs))
