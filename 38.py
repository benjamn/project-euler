from util import *

def niner(base):
    s = ""
    i = 1
    while 1:
        s += str(base*i)
        l = len(s)
        if l >= 9:
            if l == 9:
                yield s
            else:
                break
        i += 1

def solve():
    for base in range(10000):
        for n in niner(base):
            if "0" not in str(n) and pandigital(n):
                yield n

print max(solve())