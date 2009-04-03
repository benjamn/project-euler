#!/usr/bin/env python

from util import *

def gen_strs(n, d, cnt):
    if n == 0:
        return g('')
    if cnt == n:
        return g(str(d) * cnt)
    return (str(i) + prime
        for i in range(10)
        for prime in gen_strs(n - 1, d,
            cnt - (1 if i == d else 0)))

@memo
def gen_primes(n, d, cnt):
    return [int(i) for i in gen_strs(n, d, cnt)
        if i[0] != '0' and is_prime(int(i))]

@memo
def M(n, d):
    cnt = n
    while cnt > 0:
        if len(gen_primes(n, d, cnt)) > 0:
            break
        cnt -= 1
    return cnt

@memo
def N(n, d):
    return len(gen_primes(n, d, M(n, d)))
    
@memo
def S(n, d):
    return sum(gen_primes(n, d, M(n, d)))

def answer(n):
    for d in range(10):
        print "%d, %d, %d, %d" % (d, M(n, d), N(n, d), S(n, d))
    return sum(S(n, d) for d in range(10))

print answer(10)