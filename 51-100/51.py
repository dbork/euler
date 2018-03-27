# observation: these are APs with delta given by a permutation of 100...,
# 1100..., etc. with n leading 1s. therefore you can't get one with 8 primes if
# n % 3 != 0, since you'll end up with at least 3 numbers divisible by 3.

# okay, now let's get all the primes with 10.py...

# sad-person sieve
import math

limit = 10000000
loglimit = len(str(limit))
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

filteredPrimesList = filter(lambda x: x, primesList)
print "primes calculated..."

# we can safely throw out any prime that doesn't have 3 of the same digit
# and, since we're only using this to find the seeds for our equivalence
# classes, we can also get rid of all the ones whose repeated digits
# are anything other than 0, 1, or 2
filteredPrimesList = filter(lambda x: \
                     max([list(str(x).zfill(loglimit - 1)).count(i) for i in \
                     ['0', '1', '2']]) > 2, filteredPrimesList)

#print filteredPrimesList
print len(filteredPrimesList)

# so what's nice about 110? it's 1 mod 3 ofc, but it's 0 mod 2, which is
# necessary, since otherwise every other AP element would be even. it's
# 2 mod 4, which is fine -- it just mandates that we start with something that
# is 1 or 3 mod 4. it's 0 mod 5, but that's obvious, since it has to be even
# and is a permutation of 0s and 1s. we need the same property in our delta,
# so the last digit has to be 0

# anyway, let's divide the primes into equivalence classes...
import itertools as it

deltas = []

for i in range(3, loglimit, 3):
    for p in set(it.permutations([1] * i + [0] * (loglimit - i - 2))):
        deltas.append(''.join(map(str, p) + ['0']))

print deltas

APs = []

for seed in filteredPrimesList:
    strseed = str(seed).zfill(loglimit - 1)

    # we only need to actually look for APs with a few deltas...
    relevantDeltas = []
    for delta in deltas:
        if len(set([strseed[i] for i in range(loglimit - 1) \
               if delta[i] == '1'])) == 1:
            relevantDeltas.append(delta)

    for delta in relevantDeltas:
        AP = []
        AP.append(seed)
        # what number are we starting at?
        init = strseed[list(delta).index('1')]
        for j in range(1, 10 - int(init)):
            cand = seed + j * int(delta)
            if primesList[cand] != 0:
                AP.append(cand)

    APs.append(AP)

print filter(lambda x: len(x) >= 8, APs)
