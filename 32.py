from util import permutations as ps

def toi(lst):
    return int(''.join(str(e) for e in lst))

seen = set()

def search(p, al, bl, cl):
    a = toi(p[0:al])
    b = toi(p[al:al+bl])
    c = toi(p[al+bl:al+bl+cl])
    if a * b == c:
        print "%d * %d = %d" % (a, b, c)
        seen.add(c)

for p in ps([1,2,3,4,5,6,7,8,9]):
    search(p, 2, 3, 4)
    search(p, 1, 4, 4)
    
print sum(i for i in seen)
