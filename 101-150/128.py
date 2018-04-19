# hexagonal prime differences, ok
import sys
sys.path.append("..")
import primes as p

# here are some facts!

# fact 1: nothing with PD(n) = 3 can be on a "long edge" of a ring, since
# such numbers are adjacent ot their successors and predecessors (two 1s), 
# and two pairs of adjacent numbers (one of each must have even difference)
# for a max of PD(n) = 2. well, unless they're on the 7/19/37 vertical

# fact 2: 1 works. that's boring but necessary

# fact 3: as for the corners, they already have two 1s and are next to three
# consecutives. if the difference with the center consecutive is anything
# other than 0 mod 6, there are two more composite differences, and we're done,
# which already rules out all corners but the upper ones, wow

# fact 4: the upper corners and 7-19-37 vertical play by different rules.
# the upper corners have a 1 and two multiples of 6 each, so they depend on
# /both/ differences with their friends in the 7-19-37 vertical being
# prime. meanwhile the vertical folks have, wow, an exactly symmetric
# situation.

# so 7 doesn't work and 2 does by inspection. the other differences are all
# one less than a multiple of 6. they aren't all covered, but, for ring i,
# the "internal" difference (upper corner minus the lover vertical pal)
# is 6i - 1 and the "external" difference (the other one) is 6(2i + 1) - 1,
# by more-or-less inspection. this is enough that we can be procedural

# so what tile in the sequence do we want?
limit = 2000

# how many primes do we need? since there's a valid PD(n) = 3 number in
# "most-ish" of the rings, we need at most the first 6 * 4 * limit primes or
# so, being more liberal than we probably need because we can
# update: it seems that wasn't liberal enough. oh well
primesList = p.getPrimes(600 * limit, "log")
sequence = [1]

# starting with ring 2
ring = 1
current = 2
# was the last difference prime?
lastDiff = 5 

while len(sequence) <= limit:
    # wait, there's one more fact we need. differing from the next
    # vertical in the chain by a multiple of 6 does not guarantee that the
    # difference between its predecessor/successor is prime. this
    # difference also needs to be checked.

    # the first one we check is on the upper corner of ring i
    firstDiff = 6 * (2 * ring + 1) - 1
    otherDiff = lastDiff + 2
    if primesList[lastDiff] != 0 and primesList[firstDiff] != 0 \
            and primesList[otherDiff] != 0:
        sequence.append(current)

    # we then check its friend on ring i + 1
    current += firstDiff
    secondDiff = 6 * (ring + 1) - 1
    otherDiff = 6 * (ring + 2) - 1
    if primesList[firstDiff] != 0 and primesList[secondDiff] != 0 \
            and primesList[otherDiff] != 0:
        sequence.append(current)

    current -= secondDiff
    lastDiff = secondDiff
    ring += 1

print sorted(sequence)[limit - 1]
