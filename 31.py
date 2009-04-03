from util import memo

@memo
def ways(total, denoms):
    print total, denoms
    if len(denoms) == 0:
        if total == 0:
            return 1
        else:
            return 0
    else:
        x = 0
        num_ways = 0
        while x * denoms[0] <= total:
            num_ways += ways(total - x * denoms[0], denoms[1:])
            x += 1
        return num_ways

print ways(200, (1, 2, 5, 10, 20, 50, 100, 200))
