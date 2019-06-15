# so we can calculate this by going through the primes and multiplying
# all their multiples by the relevant term in the totient formula
import sys
sys.path.append("..")
import primes
import itertools as it

# i guess i don't actually know if this approach is faster than
# prime-factorizing-by-trial-division, but i think it works fast enough for
# the purposes of problem 70. but if needed, we should try to optimize
def getTotients(n):
    totients = range(n + 1)
    primesList = filter(lambda x: x != 0, primes.getPrimes(n, "log"))

    for prime in primesList:
        # since in most useful applications this is what we want, i decree that
        # primes are not relatively prime to themselves
        totients[prime] -= 1

        for i in range(2, n / prime + 1):
            totients[prime * i] *= (prime - 1) 
            totients[prime * i] /= prime

    return totients

# function that returns a modified totient consisting only of the integers i
# less than n that are relatively prime to n and such that i / n <= 1 / k for
# some user-defined k >= 2.
def getTruncatedTotients(n, k):
    totients = map(lambda x: x / k, range(n + 1))
    primesList = filter(lambda x: x != 0, primes.getPrimes(n, "log"))

    for prime in primesList:
        # we no longer need this, since p / p is way bigger then 1 / k
        #totients[prime] -= 1

        for i in range(2, n / prime + 1):
            # this is awkward because integer division means we can't
            # just multiply by (p-1)/p, so we'll exploit integer
            # division as follows: (though this doesn't work, see, eg, 12)
            totients[prime * i] -= totients[prime * i] / prime
            #totients[prime * i] *= (prime - 1) 
            #totients[prime * i] /= prime

    return totients
