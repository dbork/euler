# we only need to find the three most likely spaces, so can we
# do this without actually coding?

# for one, d4s up the odds of doubles, so JAIL should be first by
# an even more enormous margin

# then the tail extending outwards from JAIL should be more concentrated
# about JAIL than in the d6 case, which might bump Illinois (E3) down

# observe that the amount of tail that reaches E3 from JAIL in the d6 case
# is worth about an extra CH/CC, since the result is comparable with GO,
# which has essentially no JAIL tail. fattening it only needs to reduce
# the fraction that reaches E4 by a little bit to knock it down, which
# i'm pretty sure it will

# what squares does this fattening favor? not C1, which can't be reached
# from JAIL. not reeeally U1, since only 1/16 vs 1/36 runs that start
# at JAIL ever get a crack at it (and its CC is not as valaubale as the
# average one anyways). so the answer really isn't any of the
# motive squares per se...

# actually, what about the GO tail? R1 is right in the middle of it
# and is already at 1.7 CH/CC...that effect can never bring it over
# GO ofc, but maybe could push it over a weakened E3 if the tail
# is fattened enough...

# so i think my best guess is JAIL, GO, R1, with the next guess
# being JAIL, GO, E3. let's try the former...

#print 100005

# nope, not that, sorry R1 :(

#print 100024

# ooh, not that either! i wonder what i'm missing?

# maybe R2! it /is/ right in the middle of the huge JAIL monster, and
# had 2/3 of a CH already. with the old tail, that wasn't enough to push it
# past E3, let alone GO, but times have changed! let's try it in
# both positions...

#print 100015
#print 101500

# iiiinteresting. what's the deal, i wonder... maybe the fattening of
# the jail-tail is outweighed by the increased jail odds and E3 is
# still in the mix? hmmm i might have to actually do this :( that's
# annoying lmao

# ugh finee

import random

dist = [1.0 / 40 for i in range(40)]
iters = 500

for i in range(iters):
    newDist = [0 for i in range(40)]
    rolls = [0, 0, 1.0 / 16, 2.0 / 16, 3.0 / 16, 4.0 / 16, 3.0 / 16, \
             2.0 / 16, 1.0 / 16]

    # propagate via die rolls...

    for square in range(40):
        for roll in range(len(rolls)):
            newDist[(square + roll) % 40] += rolls[roll] * dist[square]

    # now handle the weird rules

    # G2J
    newDist[10] += newDist[30]
    newDist[30] = 0

    # triple doubles
    newDist[10] += (4.0 / 16) ** 3
    for i in range(40): # if i != 10:
        newDist[i] *= (1 - (4.0 / 16) ** 3)

    # CC
    for CC in [2, 17, 33]:
        newDist[0] += newDist[CC] / 16
        newDist[10] += newDist[CC] / 16
        newDist[CC] *= 7.0 / 8

    # CH
    for CH in [7, 22, 36]:
        newDist[0] += newDist[CH] / 16
        newDist[10] += newDist[CH] / 16
        newDist[11] += newDist[CH] / 16
        newDist[24] += newDist[CH] / 16
        newDist[39] += newDist[CH] / 16
        newDist[05] += newDist[CH] / 16

        rail = (((CH + 5) / 10) * 10 + 5) % 40
        util = min((12 - CH) % 40, (28 - CH) % 40)

        newDist[rail] += newDist[CH] / 8
        newDist[(CH + util) % 40] += newDist[CH] / 16
        newDist[CH - 2] += newDist[CH] / 16

        newDist[CH] *= 6.0 / 16

    dist = newDist

for i in range(40):
    print i
    print dist[i]

# and the answer is JAIL, R2, E3, so i didn't actually have to do it lmao
# but strangely enough, D1 was very in the mix just by JAIL-tail alone
# and GO was below a bunch of stuff. i guess the tail effect just got huge
# from triple-doubles and dominated everything else.

# also R1 was below GO, for reasons i can't fathom haha
# i guess maybe the combination of boardwalk and CH3 might be sapping GO
# slightly? but that's really weird and counterintuitive imo
