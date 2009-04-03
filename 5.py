
def least_div_by(factors):
    limit = reduce(lambda a, b: a * b, factors)
    return min(n for n in xrange(limit + 1)
        if all(n % factor == 0
            for factor in factors))

def answer(start, end):
    return least_div_by(xrange(start, end + 1))

print answer(1, 5)