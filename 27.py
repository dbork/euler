# can probably do exhaustive search
# look in The Notebook for math logic

# how many primes do we need? the longest sequence is bounded by |b|, since the
# b'th term is b^2 + ab + b, which is divisble by b. so the largest prime
# reachable is bounded by 1000^2 + 1000(1000) + 1000 = 2001000. so we have to
# use the problem 10 sieve.
import math

limit = 2001000
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

print "primesList calculated"

# so we /don't/ want to filter primesList this time, since we would really
# like constant-time primality checking
#primesList = filter(lambda x: x, primesList)

# non-stolen-from-problem-10 code starts here

# best has the format [length, a, b]
best = [0, 0, 0]

#for a in range(-1000, 1000):
for a in range(999, -1000, -1):
    for b in range(-1000, 1001):
        iteration = 0
        nextCandidate = b
        while nextCandidate > 0 and primesList[nextCandidate] != 0:
            iteration += 1
            nextCandidate += 2 * iteration + a - 1
        if iteration > best[0]:
            best = [iteration, a, b]
            print best
print best
