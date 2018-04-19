# so we can calculate this by going through the primes and multiplying
# all their multiples by the relevant term in the totient formula
import sys
sys.path.append("..")
import primes
limit = 20

# i guess i don't actually know if this approach is faster than
# prime-factorizing-by-trial-division, but i think it works fast enough for
# the purposes of this problem
def getTotients(n):
    totients = map(float, range(n))
    primesList = filter(lambda x: x != 0, primes.getPrimes(n, "log"))

    for prime in primesList:

getTotients(limit)

#def getPrimes(n, freq=None):
#    if freq != None:
#        print "calculating primes less than " + str(n) + "..."
#    primesList = range(n)
#    primesList[1] = 0
#
#    # since every divisor removes numbers at least twice itself, we only have
#    # to consider divisors up to limit / 2
#    for divisor in range(2, n / 2):
#        if freq != None and freq != "log" and divisor % freq == 0:
#            print "removing multiples of " + str(divisor)
#
#        if freq == "log" and math.log(divisor, 2).is_integer():
#            print "removing multiples of " + str(divisor)
#
#        if primesList[divisor] == 0:
#            continue
#        for j in range(2, (n - 1) / divisor + 1):
#            primesList[j * divisor] = 0
#
#    print "primes calculated..."
#    return primesList
