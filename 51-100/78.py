# like those tiling ones, the key here is that every parition has
# a leftmost element, since we don't want to double-count everything

# ^^ actually that's false because partitions with the same sizes are
# considered identical. the thing we want is that each partition has a
# /largest/ element

# ways [i][j] then is the number of paritions of i coins into subsets,
# the largest of which has size j
# this is needed to ensure disjointness of the partition, which is
# the way to beat double-counting
#limit = 1000

# appending to the internals of lists might be slower, so should be
# worth doing it this way

# i don't think we actually need ways, we never use it for anything
#ways = [[1], [0, 1]] # + [[0, 1] for i in range(limit)]
sumWays = [[1], [0, 1]] # + [[0, 1] for i in range(limit)]
numCoins = 1
divisor = 1000000

while sumWays[numCoins][-1] != 0: # and numCoins < limit:
    numCoins += 1

    thisWay = [0, 1]
    thisSum = [0, 1]

    # the numCoins + 1 case is the one where there is no partition
    for largest in range(2, numCoins + 1):
        nextLargest = min(largest, numCoins - largest)
        
        # do it all mod divisor or this will become unmanageably huge
        thisWay.append(sumWays[numCoins - largest][nextLargest]\
                                      % divisor)
        thisSum.append(sum(thisWay) % divisor)

    #ways.append(thisWay)
    sumWays.append(thisSum)

    if numCoins % 100 == 0:
        print numCoins
        #print ways[numCoins]
        #print sumWays[numCoins]
        print sumWays[numCoins][-1]

#print map(lambda x: x[-1], sumWays)
print numCoins
#print sumWays[5]

# this might still not be efficient enough, which means we need a closed-
# form
