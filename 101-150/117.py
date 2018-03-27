# stealing from 116 this time
limit = 50 
ways = [1, 1]
tiles = [2, 3, 4]

for length in range(2, limit + 1):
    # add some arbitrary red block somewhere and recurse
    # no wait, that double-counts, add the leftmost red block and then
    # recurse
    sumWays = 0
    for tile in range(len(tiles)):
        tileSize = tiles[tile]
        
        # edge case for tiles being too big
        if tileSize > length:
            continue

        for startPoint in range(0, length + 1 - tileSize):
            # the requirement of a black border makes this a little more
            # complicated in 114, but not here :p
            # but the requirement that the tilings be homogeneous
            # does make it tougher
            rightSize = max(0, length - (tileSize + startPoint))
            sumWays += ways[rightSize] #* ways[leftSize]

    # don't forget the all-black one
    ways.append(sumWays + 1)

print ways[limit]
