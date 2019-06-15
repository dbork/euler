# so we can calculate this by going through the primes and multiplying
# all their multiples by the relevant term in the totient formula
import sys
sys.path.append("..")
import primes
import itertools as it
limit = 10000000

# i guess i don't actually know if this approach is faster than
# prime-factorizing-by-trial-division, but i think it works fast enough for
# the purposes of this problem
def getTotients(n):
    #totients = map(float, range(n))
    totients = range(n + 1)
    primesList = filter(lambda x: x != 0, primes.getPrimes(n, "log"))

    for prime in primesList:
        for i in range(2, n / prime + 1):
            totients[prime * i] *= (prime - 1) 
            totients[prime * i] /= prime

    return totients

totients = getTotients(limit)
print "totients calculated..."
totientRatios = [0] + [float(i) / totients[i] for i in range(1, limit + 1)]
print "totient ratios calculated..."
r = range(limit + 1)

joinedList = zip(r, totients, totientRatios)
# checking whether the sorted lists of digits in i and j are equal is
# equivalent to checking whether the two are permutations of each other
print sorted(filter(lambda x: sorted(list(str(x[0]))) \
                           == sorted(list(str(x[1]))) and x[0] != x[1], \
                           joinedList), key=lambda y: y[2])[0]
