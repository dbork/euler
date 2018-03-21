# itertools.cycle combined with the primes sieve from 10.py
import itertools as it

# stolen from 10.py:
# sad-person sieve
import math

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

# commented out for constant-time access
#primesList = filter(lambda x: x, primesList)
print "calculated primes..."
# end 10.py

num = 0
# definitely could be sped up by close to a factor of 6 if needed by avoiding
# repedition, but i don't really feel like it
# oh yeah, and after running this, obviously they all have to be permutations
# of 1, 3, 7, and 9 lmao
for i in map(str, range(1000000)):
    cycle = [i[j:] + i[:j] for j in range(len(i))]
    if reduce(lambda x, y: x and y, map(lambda z: primesList[int(z)] != 0, cycle)):
        print cycle
        num += 1
print num
