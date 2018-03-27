# whelp as usual with primes, there's no easy way to deal with this lol
import sys
sys.path.append("..")
import math
import primes

# so this is too memory-intensive for dunkhut to handle.
# ...maybe, since we're not actually using that many primes, trial division
# would actually be better?
#limit = 100000000
#primesList = primes.getPrimes(limit, "log")
#print "primes calculated..."

#sideLengthLimit = 10000
primesList = [3, 5, 7]
square = 9
while float(len(primesList)) / ((((math.sqrt(square)) - 1) * 2) + 1) > 0.1: # \
    #    and square < sideLengthLimit ** 2:
    sideLength = math.sqrt(square) + 1
    for i in range(1, 5):
        square = int(square + sideLength)
        if primes.isPrime(square):
            primesList.append(square)
    print math.sqrt(square)
    print float(len(primesList)) / ((((math.sqrt(square)) - 1) * 2) + 1) 

print math.sqrt(square)
#if sideLengthLimit ** 2 == square:
#    print "which is the side length limit..."
