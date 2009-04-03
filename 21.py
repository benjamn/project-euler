from util import memo, divisors, amicable
from sys import argv

for i in xrange(int(argv[1])):
    if amicable(i):
        print i, sum(divisors(i))

