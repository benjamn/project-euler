from util import factors

def answer(n):
    return max(factors(n))
    
print answer(317584931803)
