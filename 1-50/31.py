# more dictionaries
#mc = {0: 1}

#for i in range(1, 201):
#    ways = mc[i - 1]
#    for coin in [2, 5, 10, 20, 50, 100, 200]:
#        if i >= coin:
#            ways += mc[i - coin]
#    mc[i] = ways
#print mc[5]

# ^^ that doesn't work

# \/\/ try this DP
# invariant: number of ways to make change
# using coins of that size or smaller
dp = [[0 for i in range(8)] for i in range(201)]
coins = [1, 2, 5, 10, 20, 50, 100, 200]
for amt in range(0, 201):
    dp[amt][0] = 1
    for coin in range(1, 8):
        if amt in [0, 1]:
            dp[amt][coin] = 1
        #if amt == 3:
        #    print coin
        #    print dp[amt - coins[coin]][coin] + dp[amt][coin - 1]
        #    print dp[amt][coin - 1]
        elif amt >= coins[coin]:
            dp[amt][coin] = dp[amt - coins[coin]][coin] + dp[amt][coin - 1]
        else:
            dp[amt][coin] = dp[amt][coin - 1]
        #if amt == 3:
        #    print dp[amt][coin]
    #print dp[amt]

#print dp
print dp[200][7]
