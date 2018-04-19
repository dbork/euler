# expected number of distinct colors after i picks is the
# expected number of distinct colors after i - 1 plus 7 / (7 - that)
# by linearity of expectation (at least with replacement it would be)
total = 70.0
colors = 7.0
limit = 20
DP = [1.0]

# this is tempting but simplistic, since you're sampling without
# replacement...
#for pick in range(1, limit):
#    DP.append(DP[-1] + (colors - DP[-1]) / colors)

# luckily, all of the colors are evenly distributed...
for pick in range(1, limit):
    # so the expected number of balls /remaining/ that are a color that
    # hasn't been chosen equals the expected original number of all the
    # unpicked ones (since we haven't removed any of the balls of these
    # colors) divided by the total number of balls remaining:
    DP.append(DP[-1] + ((total / colors) * (colors - DP[-1])  \
                       / (total - pick)))

print DP[-1]
