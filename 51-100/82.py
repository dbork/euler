# first, parse the input matrix
matrix = []
f = open("p082_matrix.txt")
for line in f:
    matrix.append(map(int, line.rstrip().split(',')))
f.close()

# now, dp
dp = []

# so each cell in the dp will hold the best path from /some/
# cell on the left side to this cell
# in theory, it would be nicer to flip the matrix first, but
# i'm going to favor (percieved) readability instead and not do that

# first, base case
for row in range(len(matrix)):
    dp.append([matrix[row][0]])

# now handle the rest of the matrix
for col in range(1, len(matrix[0])):
    # initialize the column assuming the best path goes right in the
    # most recent step
    accessCosts = [dp[row][-1] + matrix[row][col] \
                  for row in range(len(matrix))]
    
    # now check to see if we can beat that by moving up or down
    # but, wait, this is nontrivial, because who knows how many steps one
    # may want to go down in a row

    # hence "access cost": this is the best cost to reach this position from
    # the immediate right. to find the best cost overall, we have to do
    # another minimization
    for row in range(len(matrix)):
        cands = []
        for i in range(row):
            cands.append(accessCosts[i] + sum([matrix[j][col] \
                        for j in range(i + 1, row + 1)]))
        cands.append(accessCosts[row])
        for k in range(row + 1, len(matrix)):
            cands.append(accessCosts[k] + sum([matrix[j][col] \
                        for j in range(row, k)]))
       
        dp[row].append(min(cands))

print min([dp[row][-1] for row in range(len(matrix))])
