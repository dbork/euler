# DP
pyramid = []
f = open("p067_triangle.txt")
for line in f:
    pyramid.append(map(lambda x: int(x), line.rstrip('\n').split(' ')))
f.close()

dp = [pyramid[0]]
for i in range(2, len(pyramid) + 1):
    dp += [[0] * i]

for j in range(1, len(pyramid)):
    row = pyramid[j]
    for k in range(len(row)):
        if k == 0:
            dp[j][k] = dp[j-1][k] + row[k]
        elif k == len(row) - 1:
            dp[j][k] = dp[j-1][k-1] + row[k]
        else:
            #print j, k
            dp[j][k] = max(dp[j-1][k-1] + row[k], dp[j-1][k] + row[k])

print max(dp[len(dp) - 1])
