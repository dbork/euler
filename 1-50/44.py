# so Pn = n(3n - 1) / 2
#       = 3/2 n^2 - 1/2 n for arbitrary n
# therefore, for arbitrary i < n,
# P(n-i) = (n - i)(3n - 3i - 1) / 2
#        = 3/2 n^2 + 3/2 i^2 - 3 ni - 1/2 n - 1/2 i

# hmm this math seems rather impenetrable

# other insights:
# if we loop over the pentagonal numbers, we could ask in turn whether each
# newly-calculated one is the sum of two others, then ask for the difference,
# and stop iterating once we have some best and successive pentagonals are
# larger than that. it's brute-forcey but shouldn't take too long,
# eg O(sqrt(D)^3) where D is whatever the answer is lol. it's unsatisfying
# but it'll probably work

# periodic structure:
# mod 2: 1 1 0 0 ...
# mod 3: 1 2 0 ...
# mod 4: 1 1 0 2 3 3 2 0 ... (oh, these equal sizes are a manifestation of
# mod 5: 1 0 2 2 0 ...        Lagrange's theorem, cool! um, maybe)

# any sum or difference relations would have to hold in all of these worlds...
# are any of them especially useful? 5 is, i guess...the only valid pairs
# are 0 +- 0, 1 +- 0, and 2 +- 0. so the smaller number in any putative
# pair must be divisible by 5. that's a factor of 2 speedup i guess?
# wait, i'm lying, 1 +- 1 works too...

# is it also convenient to know that the last digit of a pentagonal can't be
# 3, 4, 8, or 9?

# wait, there's probably something much more useful. the differences
# go 4, 7, 10, ... = 3n + 1. when you have a pentagonal x and want to see if
# it's a sum, you are looping over the pentagonals p and asking if x-p and
# x-2p are both pentagonals

# fine i'll be a lame-o
bestDiff = float('inf')
n = 3
pents = [1, 5]

while pents[-1] - pents[-2] < bestDiff:
    nextPent = n * (3 * n - 1) / 2
    pents.append(nextPent)
    #print "pents so far:"
    #print pents
    #print "best diff so far: " + str(bestDiff)
    #print "next pent: " + str(nextPent)
    
    # iterate manually to save time
    diffIndex = 0

    # this is slightly wrong and could miss some that are really close
    # together, hmm...
    largerIndex = len(pents) / 2
    smallerIndex = len(pents) / 2

    if n % 10000 == 0:
        print "n = " + str(n)
        print "previous pent = " + str(pents[-2])
        print "next pent = " + str(nextPent)
        print "difference = " + str(nextPent - pents[-2])

    while pents[diffIndex] < nextPent:
        diff = pents[diffIndex]
        diffIndex += 1
        #print "diff = " + str(diff)
        #print "nextPent - diff = " + str(nextPent - diff)
        #print "nextPent - 2 * diff = " + str(nextPent - 2 * diff)
        if diff > bestDiff:
            break
       
        putativeLarger = int(float(nextPent) / 2 + float(diff) / 2 + 0.1)
        putativeSmaller = putativeLarger - diff

        while putativeLarger > pents[largerIndex]:
            largerIndex += 1
        while putativeSmaller < pents[smallerIndex]:
            smallerIndex -= 1

        #if nextPent - diff == pents[minusOneIndex]:
            #print "nextPent - diff is pentagonal!"
        #if nextPent - 2 * diff == pents[minusTwoIndex]:
            #print "nextPent - 2 * diff is pentagonal!"

        if putativeSmaller == pents[smallerIndex] \
                and putativeLarger == pents[largerIndex]:
            print "new best diff: " + str(diff)
            bestDiff = diff
            break
    
    n += 1

# in practice, the first one it came up with worked. but rigorously
# checking that it's the smallest takes forever (probably ~an hour)
print "final best diff = " + str(bestDiff)
