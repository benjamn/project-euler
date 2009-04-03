from util import fact

def sumpow(n, e):
    return sum(int(c)**e for c in str(n))
    
def sumfact(n):
    return sum(fact(int(c)) for c in str(n))
    
i = 1
while True:
    if sumfact(i) == i:
        print i
    i += 1
