from util import *

def equiv_key(n, d):
    ds = str(d)
    return ''.join(['*' if c == ds else str(c)
        for c in str(n)])

ecs = {}
def initial_answer(start):
    max = 0
    for prime in primes(start):
        for d in unique_digits(prime):
            k = equiv_key(prime, d)
            try:
                ecs[k].add(prime)
            except:
                ecs[k] = set([prime])
            cnt = len(ecs[k])
            if cnt > max:
                print k, ecs[k]
                max = cnt

def count(n, d):
    result, sn, sd = 0, str(n), str(d)
    if sd in sn:
        for i in xrange(10):
            sp = sn.replace(sd, str(i))
            if sp[0] != '0' and is_prime(int(sp)):
                result += 1
    return result
                
def answer(start):
    max = 0
    for prime in primes(start):
        for d in (0,1,2): # important!
            cnt = count(prime, d)
            if cnt > max:
                print prime, cnt, d
                max = cnt

print answer(56000)
