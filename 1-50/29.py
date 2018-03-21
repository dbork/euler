# notes on paper for this one for the most part
limit = 100

# luckily these numbers are pretty small, so we can get prime factorizations
# by trial division and not have that be prohibitively awful
def primeFac(n):
    facs = []
    k = 2
    ncurr = n
    while k <= ncurr / 2:
        if ncurr % k == 0:
            facs.append(k)
            ncurr /= k
        else:
            k += 1
    facs.append(ncurr)
    return facs

primeFacs = [primeFac(n) for n in range(2, limit + 1)]

# we're also going to kill portability by hard-coding all the powers less
# than 100, lol
powerDict = {4: [2, [2]], 8: [2, [3]], 9: [3, [2]], 16: [2, [2, 2]], \
        25: [5, [2]], 27: [3, [3]], 32: [2, [5]], 36: [6, [2]], 49: [7, [2]], \
        64: [2, [2, 3]], 81: [3, [2, 2]], 100: [10, [2]]}

import itertools

uniques = set()

for base in range(2, limit + 1):
    for exponent in range(2, limit + 1):
        # first, get the prime factorization of the exponent
        facs = primeFacs[exponent - 2]
        
        # first, see if we need to move powers up
        if base in powerDict:
            expandedFacs =  facs + powerDict[base][1]
            reducedBase = powerDict[base][0]
            expandedFacs.sort()
        else:
            expandedFacs = facs
            reducedBase = base

        # next, add the (base, factored exponent) pair to the set, if it's not
        # there already
        uniques.add((reducedBase, ' '.join(map(str, expandedFacs))))

        # next, loop over subsets of the exponent's prime factorization
        #facSubsets = set()
        #for size in range(len(facs)):
        #    for subs in itertools.permutations(facs, size):
        #        facSubsets.add(subs)
       
#print uniques
print len(uniques)
