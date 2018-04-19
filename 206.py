# the last of the 5% problems
#
# so the square is 19 digits, of the form
# 1_2_3_4_5_6_7_8_9_0
#
# trying all of the 10-digit squares is a Bad Idea
# so let's just add digits and figure it will work itself out
# eg for the last digit of n ** 2 to be 0, the last digit of n must be 0
# as well.
#
# n ** 2 = 1_2_3_4_5_6_7_8_9_0
#
# so the first two digits have to be 11, since the only two-digit squares
# under 100 are 100, 121, 144, 169, and 196. then 110^2 = 12100, and each
# additional digit in the 1s place adds 110 + 111 = 221. to get the third
# digit of n ** 2 to a 2, we need to do this 5 times.
#
# then 1150 ** 2 = 1322500. each additional ones-place digit adds 1150 + 1151
# = 2302. but we can't get that horrible 5 to be a 3 without rolling over on
# our two. backup plan: go with 1100 * 2 = 1210000 and /try/ for a rollover.
# each ones-place digit adds 2200. this also never gets us to a 3, but it
# can get us to a 2 with rollover via 1106 ** 2 = 1223236.
#
# next up, 11060 ** 2 = 122323600, and we're adding 22121. but now, horribly,
# we can /only/ get a 3 by adding this /exactly 5 times/. woof.
# 
# this gives 110650 ** 2 = 12243422500, and we're adding 221300. luckily, we
# can't murder our 3. unluckily, it's now pretty clear that this approach will
# have Big Problems with the last few digits, and isn't meaningfully reducing
# the branching factor.

# ok, remind me why we didn't do the reverse approach again? start with
# 30 ** 2 = 900. x30 ** 2 = (x00 + 30) ** 2 = 30 ** 2 + 6x000 + (x^2)0000.
# but getting an 8 in the 5th digit is impossible. so let's try 70 ** 2 = 4900.
# then x70 ** 2 = (14x)000 + (x^2)0000 + 70 ** 2, and the 5th digit is
# (x ** 2 + 6x + 4) / 100. sigh, plus some other stuff :(

# ok, new approach -- approach from both sides, maybe using an exhaustive
# search? the one thing from the above that /must/ be true is that the first
# digit must be one and the last digit 0. in theory we now only have 7 more
# digits to check, which is right about at the magical window of python
# feasibility, not that i really want to do that...

# then 10 ** 9 ** 2 is, ofc, 10 ** 18. then it is in fact true that the
# eighth digit has to be 3 or 7 and the second digit < 5, which probably
# cuts it down enough to for sure enter the window with only a million
# candidates

# that suuuucks though. ok, let's try the following
# observe that 1010101010 ** 2 = 1020304050403020100.
# then (1010101010 + x) ** 2 = that ^^ + 2020202020x + x ** 2. so if your x is,
# say, 10100, you can change some things without changing some other things

# naturally, though, i don't think that's enough to get us where we want.
# hmmmmm

#cands = ['1' + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) \
#        + str(i) + '0' for b in range(5) for c in range(10) for d in range(

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# april 10, 2018: let's try this again again, despite having spent way too much
# fruitless effort on it lol

# let x be the number, so x ** 2 = 1a2b3c4d5e6f7g8h9i0

# observe that x has to be divisible by 10, since x ** 2 is
# then x ** 2 has to be divisble by 100, and i = 0, great

# the remainder can't be divisible by either 5 or 2, i guess? for whatever
# that's worth...

# and then x ** 2 / 100 is 9 mod 10, which gives x9 = 3 or 7, and i guess we
# could make a search tree...

























