
def naive_cancel(n, d):
    s = set(c for c in str(n))
    c = s.intersection(c for c in str(d))

    if len(c) == 0 or '0' in c:
        return 0

    try:
        n = float(''.join(set(c for c in str(n)) - c))
        d = float(''.join(set(c for c in str(d)) - c))    
        return n / d
    except:
        return 0

def naive_cancel_works(n, d):
    return float(n) / d == naive_cancel(n, d)
    
for n in xrange(10, 100):
    for d in xrange(n, 100):
        if naive_cancel_works(n, d):
            print n, d
    