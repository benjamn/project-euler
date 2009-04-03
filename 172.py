
# dynamic programming!
from util import memo

# Returns number of d-digit numbers such that exactly m digits
# are repeated exactly n times:
@memo
def how_many(d, m, n):
    if d == 0:
        return 0
    if m == 0:
        pass
    # how many have
    sum(i * how_many(d, i, n - 1) for i in xrange(10))

# print how_many(5, 4)
    
# naive method
def generate(left, most=3, lst=[]):
    if left == 0:
        print lst
        return 1
    cnt = 0
    for i in xrange(10):
        if lst.count(i) < most:
            lst.append(i)
            cnt += generate(left - 1, most, lst)
            lst.pop()
    return cnt
    
def naive_gen_some_gt(d, n, lst=[]):
    if d == 0:
        for i in set(lst):
            if lst.count(i) > n:
                print lst
                return 1
        return 0
    cnt = 0
    for i in xrange(10):
        lst.append(i)
        cnt += naive_gen_some_gt(d - 1, n, lst)
        lst.pop()
    return cnt

# some number occurring 4 times but none more than 4
print naive_gen_some_gt(5, 3) - naive_gen_some_gt(5, 4)
