def count(a, b):
    seen = set()
    for a in xrange(2, a+1):
        for b in xrange(2, b+1):
            seen.add(a**b)
    return len(seen)
    
print count(100, 100)
        
