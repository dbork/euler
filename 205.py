# ok well counting works for this one, obviating thought
# no wait no it doesn't, they have a bunch of dice lolol lrn2read
# 9 * 2.5 = 22.5 > 6 * 3.5 = 21, so better than 50% lol

# then can you do it by ordering them and counting? eg say a roll is like
# P: 1 1 2 3 3 4 4 4 4
# C: 0 0 0 1 2 3 5 5 6 

# well, say P rolls first and establishes a lead between 3 and 12 on the
# first three dice. then EV is that C makes up 6 of these. so to find the
# number of winning roll seqs, we can phrase it in terms of walks about
# EV here, where we take 6 steps, EV is C gaining 1 every time, and there
# are only a few possible weighted moves...

# or maybe not about EV, just in general:
# +5, p = 1/24
# +4, p = 2/24
# +3, p = 3/24
# +2, p = 4/24
# +1, p = 4/24
# +0, p = 4/24
# -1, p = 3/24
# -2, p = 2/24
# -3, p = 1/24

# observe the symmetry! translate it about EV and you have a nice distribution
# then for say l = 7, you just need more magnitude of the right-side steps than
# left-side or center steps

# and you could totally brute-force or convolve it a bunch of times sure.
# but i want a geometric interpretation lol
