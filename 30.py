from util import fact

def sumpow(n, e):
    return sum(int(c)**e for c in str(n))
    
i = 1
while True:
    if sumpow(i, 5) == i:
        print i
    i += 1
