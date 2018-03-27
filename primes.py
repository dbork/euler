# okay, we finally need a better sieve for 58, so let's update 10.py to
# get a faster and hopefully more-definitive prime sieve.

# time to beat, for limit = 2000000:
# 
# 142913828922
#
# real	0m2.840s
# user	0m2.778s
# sys	0m0.060s

import math

# usage: getPrimes(n) returns a list of length n such that every element at
# a prime index p is p and every other element is 0. This can be indexed
# into as-is for constant-time primality checking, or filtered to give
# a list of all primes less than n.
#
# for large n, specify freq=i to print for every i sieve elements tried
# during the calculation, or freq="log" to print an update at every power of 2.

# TODO: this could likely be done much faster using a binary number and
# masking, though this loses the filterability. Try implementing that the
# next time this sieve proves insufficient for whatever reason.

def getPrimes(n, freq=None):
    if freq != None:
        print "calculating primes less than " + str(n) + "..."
    primesList = range(n)
    primesList[1] = 0

    # since every divisor removes numbers at least twice itself, we only have
    # to consider divisors up to limit / 2
    for divisor in range(2, n / 2):
        if freq != None and freq != "log" and divisor % freq == 0:
            print "removing multiples of " + str(divisor)

        if freq == "log" and math.log(divisor, 2).is_integer():
            print "removing multiples of " + str(divisor)

        if primesList[divisor] == 0:
            continue
        for j in range(2, (n - 1) / divisor + 1):
            primesList[j * divisor] = 0

    print "primes calculated..."
    return primesList

# determines whether an input is prime by trial division
def isPrime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True

# uncomment to actually do problem 10
#limit = 2000000
#primesList = getPrimes(limit)
#print sum(primesList)

# current time:
#
# 142913828922
#
# real	0m0.830s
# user	0m0.777s
# sys	0m0.052s
