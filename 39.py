from util import *

def right(a, b, c):
    return a**2 + b**2 == c**2

def triples(n):
    for c in range(1, n):
        c2 = c**2
        for b in range(1, n-c):
            b2 = b**2
            if sqrt(c2-b2) == n-c-b:
                list = [(n-c-b), b, c]
                list.sort()
                yield list[0], list[1], list[2]

def count_triples(n):
    return len(set(triples(n)))

max = 0
for n in range(1000):
    new_max = count_triples(n)
    if new_max > max:
        max = new_max
        print max, n
