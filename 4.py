def is_palindromic(n):
    sn = str(n)
    for i in xrange(len(sn) / 2):
        if sn[i] != sn[-(i+1)]:
            return False
    return True

def naive_answer():
    return max(a * b for a in xrange(100, 1000)
        for b in xrange(100, 1000)
        if is_palindromic(a * b))

print naive_answer()
