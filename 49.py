from util import *

def diffs(lst):
    return [pair[1] - pair[0]
        for pair in zip(lst, lst[1:])]

def permute(prime):
    lp = [c for c in str(prime)]
    return (int(''.join(perm))
        for perm in unique_permutations(lp)
        if perm[0] != '0')
        
def clean(perms):
    perms = [perm for perm in perms
        if is_prime(perm)]
    perms.sort()
    return perms

def prime_permutation_sets(d):
    least = least_of(d)
    return (tuple(clean(permute(p)))
        for p in bound(primes(least), least * 10))
    
def n_sets(d, n):
    for ppset in set(prime_permutation_sets(d)):
        for subset in k_subsets(ppset, n):
            yield tuple(subset)

for triple in set(n_sets(4, 3)):
    if diffs(diffs(triple))[0] == 0:
        print triple
