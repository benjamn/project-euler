for b in xrange(1000):
    a = (1000 ** 2 - 2000 * b) / (2000 - 2 * b)
    c = 1000 - a - b
    if any(i <= 0 for i in (a, b, c)):
        continue
    if a**2 + b**2 == c**2:
        print a, b, c, a*b*c