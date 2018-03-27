# this doesn't really seem that much worse than 114, so i'll steal from 114.py
#limit = 50 
m = 50
ways = [1 for i in range(m)]

length = m
while True:
#for length in range(m, limit + 1):
    sumprod = 0
    # add some arbitrary red block somewhere and recurse
    # no wait, that double-counts, add the leftmost red block and then
    # recurse
    for redSize in range(m, length + 1):
        for startPoint in range(0, length + 1 - redSize):
            # the requirement of a black border makes this a little more
            # complicated
            rightSize = max(0, length - (redSize + startPoint + 1))
            sumprod += ways[rightSize] #* ways[leftSize]

    # don't forget the all-black one
    ways.append(sumprod + 1)

    if sumprod + 1 > 1000000:
        print length
        break

    length += 1

