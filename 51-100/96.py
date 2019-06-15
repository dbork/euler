# recursion is almost never the right answer, but i think it is here
# note for future me: not really, it's still too slow, unsurprisingly.
# recursion's fine in tree search or in a DAG because you don't repeat
# calls/can easily check for cycles. but here we can't and need to
# explicitly DP. i'm tempted to just maintain a huge set of hashed
# fail-states in order to do so...
# thus, we need to be able to deep-copy stuff:
import copy
import sys

def debug(choices, nChoicePositions, pos=None, guess=None):
    print "pos:"
    print pos
    print "guess:"
    print guess
    print "choices:"
    for i in range(9):
        print choices[i]
    print "nChoicePositions:"
    for i in range(9):
        print nChoicePositions[i]

# helper for step
def update(newChoices, newNChoicePositions, pos, guess):
    if newChoices[pos[0]][pos[1]][guess - 1] > 0:
        # how many choices were there?
        oldN = len(filter(lambda x: x > 0,
                newChoices[pos[0]][pos[1]]))
        # if we are about to rule out the last valid
        # choice, we've reached an unsolvable grid
        if oldN == 1:
            return False

        # otherwise, update nChoicePositions
        newNChoicePositions[oldN].remove((pos[0], pos[1]))
        newNChoicePositions[oldN - 1].add((pos[0], pos[1]))
        newChoices[pos[0]][pos[1]][guess - 1] = 0

# helper for hashing things into the DP table
def gridToInt(grid):
    bigStr = ''
    for i in grid:
        bigStr += ''.join(map(str, i))
    return int(bigStr)

# recurse on a partially-solved grid
def step(grid, choices, nChoicePositions, DP):
    # first, check if /all/ the nonzero choice vectors are nonempty, eg
    if len(nChoicePositions[0]) == 81:
        # this means the grid is solved
        return grid

    # we should guess a value for the grid position with the fewest
    # possibilities
    for n in range(1, 9):
        if len(nChoicePositions[n]) > 0:
            # try everything
            for pos in nChoicePositions[n]:
                for guess in filter(lambda x: x > 0, choices[pos[0]][pos[1]]):
                    #print "guessing " + str(pos) + ", " + str(guess) + \
                            #" with branch factor " + str(n)
                    #print "squares remaining: " + str(81 - \
                                                      #len(nChoicePositions[0]))
                    # so if we deep-copy everything and recurse, that's bad
                    # for performance. but we have to be hacky to get around
                    # that...

                    # but the alternative is too gross to be worth it unless
                    # deep-copying for sure doesn't work lol
                    # uh and also 81 is a constant
                    newGrid = copy.deepcopy(grid)
                    newGrid[pos[0]][pos[1]] = guess
                    
                    # before doing anything else, check to see if we've made
                    # a grid that is known to be bad
                    if gridToInt(newGrid) in DP:
                        #print "encountered hash collision"
                        continue

                    newChoices = copy.deepcopy(choices)
                    newNChoicePositions = copy.deepcopy(nChoicePositions)

                    newChoices[pos[0]][pos[1]] = [0 for i in range(9)]
                    newNChoicePositions[n].remove(pos)
                    newNChoicePositions[0].add(pos)
                    
                    # horrible duplicate code means i turned this into a helper
                    # function with, uh, side-effects...it returns false if
                    # we've reached a Loss State by taking this guess
                    for otherRow in range(9):
                        if update(newChoices, newNChoicePositions, \
                                (otherRow, pos[1]), guess) == False:
                            #print "bad guess: made a position unsatisfiable"
                            DP.add(gridToInt(newGrid))
                            return False

                    for otherCol in range(9):
                        if update(newChoices, newNChoicePositions, \
                                (pos[0], otherCol), guess) == False:
                            #print "bad guess: made a position unsatisfiable"
                            DP.add(gridToInt(newGrid))
                            return False

                    for blockRow in range(3 * (pos[0] / 3), \
                                          3 * ((pos[0] / 3) + 1)):
                        for blockCol in range(3 * (pos[1] / 3), \
                                              3 * ((pos[1] / 3) + 1)):
                            if update(newChoices, newNChoicePositions, \
                                    (blockRow, blockCol), guess) == False:
                                #print "bad guess: made a position unsatisfiable"
                                DP.add(gridToInt(newGrid))
                                return False

                    # now that we've updated everything, we can recurse
                    result = step(newGrid, newChoices, newNChoicePositions, DP)
                    # if this returns an actual grid, that grid is solved
                    if result != False:
                        #print "ran out of guesses, returning"
                        return result

    else:
        # we've tried all possible guesses, and none of them worked,
        # so the grid can't be solved; return to the calling function
        DP.add(gridToInt(grid))
        return False

def solve(grid):
    # first, preprocess; we want finding the element with the fewest remaining
    # possibilities to be easy, but without making updating it hard. arrays
    # of sets should be pointers acc to owen
    nChoicePositions = [set() for i in range(10)]
    choices = [[range(1, 10) for i in range(9)] for j in range(9)]

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # need to remove this from the choice lists of elements
                # in the same row, column, or block
                num = grid[i][j]
                choices[i][j] = [0 for k in range(9)]
                for otherRow in range(9):
                    choices[otherRow][j][num - 1] = 0
                for otherCol in range(9):
                    choices[i][otherCol][num - 1] = 0
                for blockRow in range(3 * (i / 3), 3 * ((i / 3) + 1)):
                    for blockCol in range(3 * (j / 3), 3 * ((j / 3) + 1)):
                        choices[blockRow][blockCol][num - 1] = 0

    # now we can populate nChoicePositions
    for i in range(9):
        for j in range(9):
            numChoices = len(filter(lambda x: x > 0, choices[i][j]))
            nChoicePositions[numChoices].add((i, j))

    #debug(choices, nChoicePositions)
    
    # we need a DP table to make this actually feasible, so we'll make it
    # a global and then modify it in step lol
    DP = set()

    # then, note that this is the rare problem where recursion works
    # efficiently, which is something i should have figured out pre-this
    # most recent set of interviews lol
    output = step(grid, choices, nChoicePositions, DP)
    #for i in range(9):
    #    print output[i]
    return output

# now to actually open the file and do the thing
total = 0
problem = 1
f = open("./p096_sudoku.txt")
for line in f:
    if line[0] == 'G':
        grid = []
    else:
        grid.append(map(int, list(line.rstrip())))
    if len(grid) == 9:
        print "solving problem " + str(problem) + ":"
        for g in grid:
            print g
        out = solve(grid)
        total += out[0][0] * 100 + out[0][1] * 10 + out[0][2]
        print "problem "+ str(problem) + " solution:"
        for o in out:
            print o
        print "total = " + str(total)
        problem += 1
print total
f.close()
