# assume M > N

# next, note that we can close-form this; for every rectangle, there
# are a number of them equal to the number of bottom-right corners
# eg, for an M x N big rectangle and m x n small one, there are
# (M - m + 1)(N - n + 1) small ones

# so it's the sum over m, n of mn, which is also the total number of
# squares in all the upper-left subrectangles...

# (1 + 2 + 3 + ... + M)(1 + 2 + 3 + ... + N)
# = M(M+1)N(N+1)/4

# finally, loop over them diagonally, halting when N=1 gives > 2000000
def recs(M, N):
    return M * (M + 1) * N * (N + 1) / 4

target = 2000000
best = target - 1
bestArea = 1
M = 2
N = 1

while recs(M, 1) < target:
    while N <= M:
        cand = recs(M, N)
        if abs(target - cand) < best:
            best = abs(target - cand)
            bestArea = M * N
        N += 1
    M += 1
    N = 1

print target - best
print bestArea
