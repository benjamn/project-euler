from dp import memo

def g(*args):
    return (x for x in args)
    
def seq(*seqs):
    return (x for x in seq for seq in seqs)

def bound(seq, max):
    for x in seq:
        if x > max:
            break
        else:
            yield x
    raise StopIteration()

def fibs():
    a, b = 0, 1
    while True:
        yield a
        temp = a + b
        a = b
        b = temp
        
@memo
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
    
def unique_digits(n):
    digits = [False] * 10
    while n > 0:
        digits[n % 10] = True
        n /= 10
    return (d for d, b in enumerate(digits) if b)
    
def is_palindromic(n):
    sn = str(n)
    for i in xrange(len(sn) / 2):
        if sn[i] != sn[-(i+1)]:
            return False
    return True

def bin_compr(lst, elem):
    if len(lst) == 0 or lst[-1][1] != elem:
        lst.append([1, elem])
    else:
        lst[-1][0] += 1
    return lst

def compress(lst):
    return map(tuple, reduce(bin_compr, [[]] + lst))
    
def k_subsets(lst, k):
    lst = list(lst)
    if k == 0:
        return [[]]
    if len(lst) == k:
        return [lst]
    if len(lst) < k:
        return []
    rest_with = [[lst[0]] + smaller
        for smaller in k_subsets(lst[1:], k - 1)]
    rest_sans = k_subsets(lst[1:], k)
    return rest_with + rest_sans

def least_of(n):
    return int('1' + ('0' * (n - 1)))
    
def amicable(n):
    amicus = sum(divisors(n))
    return n != amicus and n == sum(divisors(amicus))

    