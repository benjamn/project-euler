from math import sqrt
from util import *

n = 1
factor = 100000

odds = set(xrange((n-1) * factor + 1, n * factor, 2))

def is_square(n):
    return sqrt(n) ** 2 == n

def cbw_primes(composite):
    for prime in bound(primes(), composite):
        less_prime = composite - prime
        if less_prime % 2 == 0:
            if is_square(less_prime / 2):
                return True
    return False

def cbw_squares(c):
    n = 0
    while 2*n**2 < c:
        if is_prime(c - 2*n**2):
            return True
        n += 1
    return False

for c in odds:
    if not is_prime(c):
        if not cbw_squares(c):
            print c

# @memo
# def compose(prime, base):
#     return prime + base ** 2

# for prime in primes():
#     for base in range(1, 100):
#         composite = compose(prime, base)
#         if composite in candidates:
#             candidates.remove(composite)
#     print len(candidates)
#     if len(candidates) < 10:
#         break
# 
# print candidates
