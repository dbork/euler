# this is one less than the coin partitions one evaluated at 100
limit = 100
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

print sumWays[-1][-1] - 1
# well, i guess the 3 hours i spend failing to solve 78 paid off in
# the form of solving this one in about 30 seconds lmao
