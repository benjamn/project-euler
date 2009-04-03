#!/usr/bin/env python

from util import fact

def answer(n):
    return sum(int(c) for c in str(fact(n)))
    
print answer(100)
