# game thing, which seems DP-able
import math
limit = 51
#nextMoverWins = [-1 for i in range(limit)]

# initial conditions
# this "0" refers to the fact that /optimal/ play by both players will
# lead the first mover to lose a subgame of size 1
#nextMoverWins[0] = 0
#nextMoverWins[1] = 0
#nextMoverWins[2] = 1
nextMoverWins = [0, 0, 1]

# we're using strings instead of lists to take advantage of xor, horrible
# though that may be
#nextMoverWins = "001"
# never mind

for stripLength in range(3, limit):
    #if math.log(stripLength, 2).is_integer():
    #    print "calculating for strip length " + str(stripLength) + "..."
    if stripLength % 10000 == 0:
        print "calculating for strip length " + str(stripLength) + "..."

    # the current player (henceforth player 1) can pick a move
    # each move divides the game into two subgames
    
    # if player 2 loses both, then player 1 wins,
    # since player 2, after losing the first subgame, then has to move
    # first in the next subgame as well
    
    # if player 2 loses one and wins the other, they win
    # overall, eg, by playing the winning subgame first and forcing player 1
    # to start the losing subgame

    # if player 2 wins them both though, they lose overall! because if they
    # play and win one subgame, player 1 gets to start and wins the next one

    # so player 1 needs to divide the strip into two subgames such that either
    # both are winning subgames or both are losing subgames, and they win
    # if there is any way to do this

    # wait, this is flawed, consider n = 9. this gives player 1 winning
    # the 3, 4 subgame. in reality though /player 2 can stall/ by
    # not playing the 4 subgame to win and salvage the scenario.
    # so we need our recursion depth to go up by 1, basically. in the 1, 0
    # case, player 2 can start the winnable subgame and then play responsively
    # forever, which should guarantee a win, fine. if neither is winnable,
    # player 1 can play responsively and that's also fine. but if both are...
    # if both are, player 2 is walking into a trap by winning the first one,
    # and the solution may honestly be just to recurse.

    # ok, so this is pretty hard. reasonable lol. so what player 2 wants is
    # to /not/ have it end up 1, 0, 0 after recursing on the right side,
    # since p1 then wins by playing reactively.

    # but iterating through this is, of course, terrible from an efficiency
    # perspective. my first instinct is apparently to do it with bitwise xor,
    # though this creates some Representational Difficulties, since we can
    # xor a string representation of the win table with an offset one and
    # get a string that is identically one if and only if player 1 has no
    # winning move
    print stripLength
    leftSubgames = nextMoverWins[:stripLength - 1]
    rightSubgames = nextMoverWins[stripLength - 2::-1]#[::-1]
    print leftSubgames
    print rightSubgames

    # wait this is way worse than the for loop
    #xored = int(leftSubgames, 2) ^ int(rightSubgames, 2)
    #print "xored: " + str(xored)
    
    # if this is identically zero, player one has no winning move
    #if xored + 1 == 1 << stripLength - 1:
    #    nextMoverWins = nextMoverWins + '0'
    #else:
    #    nextMoverWins = nextMoverWins + '1'

    for i in range(len(leftSubgames)):
        if leftSubgames[i] ^ rightSubgames[i] == 0:
            nextMoverWins.append(1)
            break
    else:
        nextMoverWins.append(0) 

    #print "nextMoverWins: " + nextMoverWins

print sum(map(int, list(nextMoverWins)))
