# like those tiling ones, the key here is that every parition has
# a leftmost element, since we don't want to double-count everything

# ^^ actually that's false because partitions with the same sizes are
# considered identical. the thing we want is that each partition has a
# /largest/ element

# ways [i][j] then is the number of paritions of i coins into subsets,
# the largest of which has size j
# this is needed to ensure disjointness of the partition, which is
# the way to beat double-counting
limit = 10000
ways = [[1]] + [[0, 1] for i in range(limit)]
sumWays = [[1]] + [[0, 1] for i in range(limit)]
numCoins = 1
divisor = 1000000

while sumWays[numCoins][-1] % divisor != 0 and numCoins < limit:
    numCoins += 1

    if numCoins % 100 == 0:
        print numCoins

    # the numCoins + 1 case is the one where there is no partition
    for largest in range(2, numCoins + 1):
        nextLargest = min(largest, numCoins - largest)
        ways[numCoins].append(sumWays[numCoins - largest][nextLargest])
        sumWays[numCoins].append(sum(ways[numCoins]))

print map(lambda x: x[-1], sumWays)
print numCoins
