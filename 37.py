from util import *

def left_decompose(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:])

def right_decompose(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[:i+1])

def ambitruncatable(n):
    return (all(is_prime(n) for n in left_decompose(n)) and
            all(is_prime(n) for n in right_decompose(n)))

def ambis():
    for p in primes():
        if ambitruncatable(p):
            yield p

def solve():
    sum = 0
    for a in ambis():
        if a > 9:
            sum += a
            print sum

solve()
