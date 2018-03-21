# so how do we cut down on the need to get all the 9-digit primes?
# step 1: it can't be 9 or 8 digits, since 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
# is 0 mod 3, as it remains when one subtracts 9. it'd be great if we could
# avoid getting all the primes up to ~8 million too, but it's not immediately
# clear how. oh well, our 10.py sieve is strong enough to do that:

# sad-person sieve
import math

limit = 8000000
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
#print sum(primesList)
print "primes calculated..."

# i'm not going to calculate or save all the permutations for this, so i'll
# just use a small silly function to do it:
def isPandigital(n):
    digitsMissing = filter(lambda x: x not in list(str(n)), \
                           map(str, range(1, len(str(n)) + 1)))
    return not sum(map(int, digitsMissing))

print max(filter(isPandigital, primesList))
# and indeed the result is 7 digits, so it's not clear how to easily do better
