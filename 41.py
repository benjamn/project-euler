from util import permutations, is_prime

def prime_perms(r):
    for perm in permutations(range(1, r)):
        n = int(''.join(str(c) for c in perm))
        if is_prime(n):
            yield n
            
print max(prime_perms(8))
