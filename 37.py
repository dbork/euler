# first, steal from 10.py as usual

# sad-person sieve
import math

# we don't know a bound on how many primes we need, unfortunately...
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

print "primes calculated..."
# comment this out as usual for constant-time accessing
primesListFiltered = filter(lambda x: x, primesList)
#print sum(primesList)

# ok, let's not make the same mistake as last time... first up, clearly
# every truncatable prime must be a permutation of 1, 3, 7, 9, since otherwise
# we can truncate from the right until we get something either even or
# divisible by 5.

# they also all must both start and end with 7 or 3, as you
# otherwise could truncate until you get 9 or 1

# next up is mod 3: they can only have up to two elements of the set {1, 7}
# or you can truncate until the result is divisble by 3...huh, i never realized
# this, but that test works exactly because 10 is 1 mod 3 (and 9). so something
# analogous holds for eg hex number with respect to divisibility by 5, neat

# we should be able to use this to bound the largest truncatable...it can have
# a {3, 7} bookend, up to two additional elements of {1, 7}, and...arbitrarily
# many 3s or 9s, sigh. i'm honestly probably just going to guess.

# ok, what's left. we need 11, and 3797 immediately gives not 5, as we might
# hope, but 3, including 37 and 797 but not 97, 79, or 379. we do also get 73
# for free by inspection.

# now we need to try inserting stuff from the set of length-n combinations of
# {1, 3, 7, 9} into the middle of each element of {33, 37, 73, 77}

import itertools as it

truncatables = set()
# waaaait my previous logic is not quite right...2 and 5 are okay but only
# at the leftmost end
#ends = ["33", "37", "73", "77", "23", "27", "53", "57"]
#i = 0

# luckily, the problem statement gives us a bound :)
#while len(truncatables) < 11 and i <= math.log(limit, 10) - 2:
#    for c in it.combinations_with_replacement('1379', i):
#        comb = ''.join(c)
        
        # this is atrocious and can surely be done better
        # but something like it is needed to avoid int('') calls
#        if comb == '':
#            intcomb = 0
#        else:
#            intcomb = int(comb)

#        for end in ends:
            # modularity test, which saves a little time
#            if (int(end) + intcomb) % 3 == 0:
#                continue
for prime in primesListFiltered:
    candidate = list(str(prime))

            #else:
            #    candidate = list(end[0] + comb + end[1])
    left = map(lambda x: primesList[int(''.join(candidate[:x]))] != 0, \
                           range(1, len(candidate) + 1))
    right = map(lambda x: primesList[int(''.join(candidate[x:]))] != 0, \
                            range(len(candidate)))
                #print candidate
                #print "left"
                #print map(lambda x: int(''.join(candidate[:x])), \
                #           range(1, len(candidate) + 1))
                #print left
                #print "right"
                #print map(lambda x: int(''.join(candidate[x:])), \
                #            range(len(candidate)))
                #print right
    if reduce(lambda x, y: x and y, left) and \
       reduce(lambda x, y: x and y, right):
           truncatables.add(int(''.join(candidate)))
           print candidate
    #i += 1
print truncatables
print sum(truncatables) - 17
