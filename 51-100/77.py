# kinda boring but straightforward DP i think
import sys
sys.path.append("..")
import math
import primes

primesList = primes.getPrimes(1000000, "log")

def isPrime(n):
    return primesList[n] != 0

filteredPrimesList = filter(isPrime, primesList)

# DP[i][j] should hold the number of ways to make i using primes
# no larger than the jth prime
DP = [[1], [0]]

n = 2
combSum = 0

while combSum <= 5000:
    i = 1
    # there's one way to make n out of primes no greater than 2 if
    # n is divisble by 2, otherwise there are no ways
    ways = [1 - n % 2]

    while filteredPrimesList[i] <= n:
        prime = filteredPrimesList[i]
        waysUsingPrime = 0

        for pmult in range(0, n / prime + 1):
            remainder =  n - pmult * prime
            if remainder == n:
                waysUsingPrime += ways[i - 1]
            else:
                waysUsingPrime += DP[remainder][min(i - 1, \
                                                len(DP[remainder]) - 1)]

        ways.append(waysUsingPrime)
        i += 1

    DP.append(ways)
    combSum = ways[-1]
    n += 1

print n - 1
