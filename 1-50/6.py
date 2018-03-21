# it's the sum of the cross-terms
nmax = 100
nsum = (nmax + 1) * nmax / 2
cross = 0

for i in range(nmax):
    cross += (i + 1) * (nsum - (i + 1))

print cross
