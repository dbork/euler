# i can't think of a better way to do this than reimplementing long division
longestRepeat = [0, 0]
#quotient = []
#nums = [10]

# keep track of the states; if we've reached one we've been to before, then
# there's a cycle
for denom in range(2, 1001):
    states = []
    currentState = (1, 0)
    while True:
        currentState = ((10 * currentState[0]) % denom, \
                        (10 * currentState[0]) / denom)
        if currentState[0] == 0:
            break
        if currentState in states:
            repeatLength = len(states) - states.index(currentState)
            if repeatLength > longestRepeat[0]:
                longestRepeat[0] = repeatLength
                longestRepeat[1] = denom
                #print "new longest repeat: " + str(repeatLength)
            break
        states.append(currentState)
    #print denom
    #print states
print longestRepeat

