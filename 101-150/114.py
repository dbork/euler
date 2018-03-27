# this shouldn't be too hard...? looks like just recursive combinatorics
limit = 50 
ways = [1, 1, 1]

for length in range(3, limit + 1):
    sumprod = 0
    # add some arbitrary red block somewhere and recurse
    # no wait, that double-counts, add the leftmost red block and then
    # recurse
    for redSize in range(3, length + 1):
        for startPoint in range(0, length + 1 - redSize):
            # the requirement of a black border makes this a little more
            # complicated
            rightSize = max(0, length - (redSize + startPoint + 1))
            sumprod += ways[rightSize] #* ways[leftSize]

    # don't forget the all-black one
    ways.append(sumprod + 1)

print ways[limit]
