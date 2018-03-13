# can probably do exhaustive search
# look in The Notebook for math logic

# best has the format [length, a, b]
best = [0, 0, 0]

# how many primes do we need? the longest sequence is bounded by |b|, since the
# b'th term is b^2 + ab + b, which is divisble by b. so the largest prime
# reachable is bounded by 1000^2 + 1000(1000) + 1000 = 2001000. so we have to
# use the problem 10 sieve.

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        iteration = 0
        nextCandidate = b
        while b in primes:
