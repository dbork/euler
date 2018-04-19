# first, parse the input matrix
matrix = []
f = open("p081_matrix.txt")
for line in f:
    matrix.append(map(int, line.rstrip().split(',')))
f.close()

# now, dp
dp = []

# base case
dp.append(map(lambda i: sum(matrix[0][:i + 1]), range(len(matrix[0]))))

for i in range(1, len(matrix)):
    row = matrix[i]
    # base case for this row
    dpRow = [row[0] + dp[i - 1][0]]
    for j in range(1, len(row)):
        el = row[j]
        dpRow.append(min(el + dpRow[j - 1], el + dp[i - 1][j]))

    dp.append(dpRow)

print dp[-1][-1]
