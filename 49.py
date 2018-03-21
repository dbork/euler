# the first step, as usual, is to plagairize 10.py to get all the primes

# sad-person sieve
import math

limit = 10000
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

# get rid of all the ones that aren't four digits
primesList = primesList[1000:]

#filteredPrimesList = filter(lambda x: x, primesList)
#print primesList

import itertools

# next, divide the primes into equivalence equives based on permutations:
equivs = []
for index in range(len(primesList)):
    if primesList[index] == 0:
        continue
    else:
        prime = index + 1000
        primesList[index] = 0
        equiv = [prime]

        # perms, nicely enough, gives this in sorted order
        for perm in itertools.permutations(str(prime)):
            cand = int(''.join(perm))
            if cand > 1000 and primesList[cand - 1000] != 0:
                equiv.append(cand)
                primesList[cand - 1000] = 0
        equivs.append(equiv)

# we can also get rid of all the equives with fewer than three elements, which
# cannot contain any 3-arithmetic progressions
equivs = filter(lambda x: len(x) > 3, equivs)

# now just manually search for APs in O(k^2), where k is the size of the
# largest equiv (eg small)
for equiv in equivs:
    for midIndex in range(1, len(equiv)):
        for smallIndex in range(midIndex):
            if 2 * equiv[midIndex] - equiv[smallIndex] in equiv:
                print str(equiv[smallIndex]) + ", " + str(equiv[midIndex]) \
                        + ", " + str(2 * equiv[midIndex] - equiv[smallIndex])

