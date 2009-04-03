from dp import memo
from math import sqrt

def first_factor(n):
    if n % 2 == 0:
        return 2
    limit = int(sqrt(n)) + 1
    for factor in xrange(3, limit, 2):
        if n % factor == 0:
            return factor
    return n
    
def factors(n):
    while n > 1:
        factor = first_factor(n)
        yield factor
        n /= factor
    
def divisors(n):
    candidates = (i+1 for i in xrange(n / 2))
    return (i for i in candidates if n % i == 0)

@memo
def is_prime(n):
    return n > 0 and first_factor(n) == n

def primes(start=2):
    if start == 2:
        yield start
    n = start / 2 * 2 + 1
    while True:
        if is_prime(n):
            yield n
        n += 2

