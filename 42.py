from util import *
from words import words

def trig(n):
    return n*(n+1)/2

def trigs():
    i = 1
    while 1:
        yield trig(i)
        i += 1

triangles = set(bound(trigs(), 1000))

@memo
def chval(ch):
    return "_abcdefghijklmnopqrstuvwxyz".find(ch)

@memo
def wval(word):
    word = word.lower()
    return sum(chval(ch) for ch in word)

def triangle(word):
    return wval(word) in triangles

def solve():
    count = 0
    for word in words:
        print word
        if triangle(word):
            count += 1
            print word, wval(word)
    print count

solve()
