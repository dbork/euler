# stealing from 10.py, as usual:

# sad-person sieve
import math

limit = 1000000
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

# this only has length ~6000, making brute-force not-completely-infeasible...
usablePrimesList = filter(lambda x: x, primesList[:60000])
#print sum(primesList)
print "primes calculated..."

# one observation: since we know the longest sequence is at least 21, the 
# smallest prime in the best sequence is bounded by 1000000/20 = 50000
# we can also bound the longest possible sequence by ~sqrt(1000000) = 1000
# but other than that, the primes are so irregularly-distributed that i'm
# not sure we can do better than trying all the (odd-length) sequences...

# let's naively do that and see how bad it is...
best = 21
numBest = 953
for l in range(21, 1003, 2):
    for i in range(len(usablePrimesList) - l):
        cand = sum(usablePrimesList[i:i + l])
        if cand >= 1000000:
            break
        if primesList[cand] != 0:
            best = l
            numBest = cand
print numBest
