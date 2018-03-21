# sad-person sieve
import math

limit = 2000000
primesList = range(limit)
primesList[1] = 0

# since every divisor removes numbers at least twice itself, we only have
# to consider divisors up to limit / 2
for divisor in range(2, limit / 2):
    # each divisor only needs to account for multiples of up to
    # its square, and should not remove itself, either
    for j in range(2 * divisor, min(divisor ** 2 + 1, limit), divisor):
        # today i learned delete in python is O(n)
        primesList[j] = 0

primesList = filter(lambda x: x, primesList)
print sum(primesList)
