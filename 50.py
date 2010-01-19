from util import *

sums = [0]
for p in bound(primes(), 10000):
    sums.append(sums[len(sums)-1] + p)

@memo
def sum_n_primes_range(b, e):
    return sums[e] - sums[b]

max_len = 0
for b in range(100):
    for e in range(b, 1000):
        total = sum_n_primes_range(b, e)
        if (total < 10**6 and
            is_prime(total) and
            e - b > max_len):
            max_len = e - b
            print total
