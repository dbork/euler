# let's see how many numbers we can prime-factorize in reasonable time...
# answer: about 100000. that's probably good enough for this one
limit = 200000

# brute-force prime factorizer from 29.py
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

    # now count them
    countedFacs = {}
    for fac in facs:
        if fac in countedFacs:
            countedFacs[fac] += 1
        else:
            countedFacs[fac] = 1

    return countedFacs

#primeFacs = [primeFac(n) for n in range(2, limit + 1)]
primeFacs = []
for i in range(2, limit + 1):
    if i % 10000 == 0:
        print i
    primeFacs.append(primeFac(i))

print "prime factors calculated"

# now to loop through this thing and look for distinct factors
for j in range(2, limit - 5):
    factorSet = set()
    for next in range(4):
        factorSet = factorSet.union(set((key, primeFacs[j - 2 + next][key]) \
                for key in  primeFacs[j - 2 + next].keys()))
    
    if len(factorSet) >= 16:
        print j
        print primeFacs[j - 2]
        print primeFacs[j - 2 + 1]
        print primeFacs[j - 2 + 2]
        print primeFacs[j - 2 + 3]
        print factorSet
        break
