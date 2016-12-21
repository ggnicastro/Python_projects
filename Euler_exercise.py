
# 500 divisors
import math
import operator
def triangle(n):
    if n == 1:
        return n
    else:
        return (n*(n+1))/2
def prime_factorize(n):
    factors = []
    number = math.fabs(n)

    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number = operator.idiv(number,factor)
    return tuple(factors)
def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2
    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x

def n_divisor(triang):

for x in xrange(1,10**9):

    triang = triangle(x)
    print triang, " *** ", x
    n_div = n_divisor(triang)
    if n_div == 500:
        print "*"*40
        print x
        break
    else:
        print n_div
        continue


