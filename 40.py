from util import *

def digits():
    i = 1
    while 1:
        for d in str(i):
            yield int(d)
        i += 1

ds = [None]

limit = 1000000
for d in digits():
    if limit > 0:
        ds += [d]
    else:
        break
    limit -= 1

print ds[1] * ds[10] * ds[100] * ds[1000] * ds[10000] * ds[100000] * ds[1000000]
