from util import *

@memo
def tri(s, a, b, c):
    return int(s[a-1] + s[b-1] + s[c-1])

def check(n):
    return (tri(n, 8, 9, 10) % 17 == 0 and
            tri(n, 7, 8, 9) % 13 == 0 and
            tri(n, 6, 7, 8) % 11 == 0 and
            tri(n, 5, 6, 7) % 7 == 0 and
            tri(n, 4, 5, 6) % 5 == 0 and
            tri(n, 3, 4, 5) % 3 == 0 and
            tri(n, 2, 3, 4) % 2 == 0)

for perm in permutations([0,1,2,3,4,5,6,7,8,9]):
    s = "".join(str(d) for d in perm)
    if check(s):
        print s
        