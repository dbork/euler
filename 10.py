# sad-person sieve
import math

limit = 2000000
primesList = range(2, limit)
divisor = 1

# since every divisor removes numbers at least twice itself, we only have
# to consider divisors up to limit / 2
for divisor in range(1, (limit + 3) / 2):
    if divisor % 10 == 0:
        print "considering " + str(divisor) + " as divisor..."
        #print primesList
    print "considering " + str(divisor) + " as divisor..."

    # each divisor only needs to account for multiples of up to
    # its square, and should not remove itself, either
    
    # here's an optimization: if j /is/ in primesList, it has to be
    # one of the first j elements
    # ...and, indeed, it must be no more than j away from the last one    
    lastIndex = 0
    nextIndex = divisor 
    for j in range(2 * divisor, min(divisor ** 2 + 1, limit), divisor):
        # find the index of the candidate, if there is one
        print "looking for " + str(j) + " here: " \
                 + str(primesList[lastIndex:nextIndex])
        try:
            loc = primesList[lastIndex:nextIndex].index(j)
            print "removing " + str(j)
            del primesList[lastIndex + loc]
            lastIndex = lastIndex + loc
            nextIndex = loc + divisor
            print "lastIndex: " + str(lastIndex)
            print "nextIndex: " + str(nextIndex)
        except ValueError:
            nextIndex += divisor
            continue

#print primesList
print sum(primesList)
