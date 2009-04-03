from util import *

def answer(limit):
    return sum(bound(primes(), limit - 1))
    
print answer(1000000)
