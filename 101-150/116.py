# more stealing from 114!
limit = 50 
ways = [[0, 0], [0, 0], [0, 0]]
tiles = [2, 3, 4]

for length in range(2, limit + 1):
    # add some arbitrary red block somewhere and recurse
    # no wait, that double-counts, add the leftmost red block and then
    # recurse
    for tile in range(len(tiles)):
        sumWays = 0
        tileSize = tiles[tile]
        
        # edge case for tiles being too big
        if tileSize > length:
            ways[tile].append(0)
            continue

        for startPoint in range(0, length + 1 - tileSize):
            # the requirement of a black border makes this a little more
            # complicated in 114, but not here :p
            # but the requirement that the tilings be homogeneous
            # does make it tougher
            rightSize = max(0, length - (tileSize + startPoint))
            sumWays += ways[tile][rightSize] + 1 #* ways[leftSize]

        # don't forget the all-black one
        # ^^ was a concern back when the all-black one was allowed
        ways[tile].append(sumWays)

#print ways
print sum([ways[tile][limit] for tile in range(len(tiles))])
