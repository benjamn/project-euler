#!/usr/bin/env python

from math import *

def log_10(n):
    return log(n) / log(10)

phi = (1 + sqrt(5)) / 2

def answer(num_digits):
    return int(ceil((num_digits-1 + log_10(5) / 2)
        / log_10(phi)))

print answer(1000)
