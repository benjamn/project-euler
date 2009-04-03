#!/usr/bin/env python

from util import bound, fibs

def answer(max):
    evens = (i for i in fibs() if i % 2 == 0)
    return sum(i for i in bound(evens, max))
    
print answer(10**6)
