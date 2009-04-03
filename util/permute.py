from dp import memo

def ins(lst, e, i):
    copy = lst[:]
    copy.insert(i, e)
    return copy
    
def next_permutation(lst):
    pass

def permutations(lst):
    if len(lst) < 2:
        yield lst
    else:
        for perm in permutations(lst[1:]):
            for i in xrange(len(lst)):
                yield ins(perm, lst[0], i)
    raise StopIteration()
    
def unique_permutations(lst):
    seen = set()
    for p in permutations(lst):
        p = tuple(p)
        if not p in seen:
            yield p
        seen.add(p)
    raise StopIteration()
    
@memo
def fact(n):
    if n <= 0:
        return 1
    return n * fact(n - 1)