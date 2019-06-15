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

k i did it on my phone lmao

why am i doing this

9d4 vs 6d6

1d4
1 2 3 4
1/4 1/4 1/4 1/4
2d4 1d4 convolve 1d4, denom=16
2 3 4 5 6 7 8
1 2 3 4 3 2 1
3d4 = 1d4 conv 2d4, denom=64
3 4 5 6 7 8 9 10 11 12
1 3 6 10 12 12 10 6 3 1

2d6 = 1d6 conv 1d6, denom = 36
-2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12
1 2 3 4 5 6 5 4 3 2 1

then one meta-round of 3 is those two convolved, with denom (64 * 36)
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10
ugh this sucks just write a function

oooor use an online convolver :)
which gives
1 5 15 35 67 111 163 215 258 282 282 258 215 163 111 67 35 15 5 1 
then convolve that with itself uh 3 times to get uhhh

1 15 120 680 3051 11493 37674 110070 291546 708998 1598430 3366402 6663781 12460203 22098780 37302852 60103530 92662038 136976800 194491392 265651653 349490603 443338470 542753082 641738313 733267143 810060822 865512042 894595248 894595248 865512042 810060822 733267143 641738313 542753082 443338470 349490603 265651653 194491392 136976800 92662038 60103530 37302852 22098780 12460203 6663781 3366402 1598430 708998 291546 110070 37674 11493 3051 680 120 15 1 

hahaha ok. and the denominator is (32*64)^3
the range meanwhile is -55 to 30. so winning scenarios for triangle are
894595248 894595248 865512042 810060822 733267143 641738313 542753082 443338470 349490603 265651653 194491392 136976800 92662038 60103530 37302852 22098780 12460203 6663781 3366402 1598430 708998 291546 110070 37674 11493 3051 680 120 15 1 
then ask wolfram to sum and divide
ok, wolfram doesn’t like that. use the convolver witha bunch of 1/30s i guess hehe

or ask the internet for a summer, which gives 7009890480, which divides to 0.5731440768 or so. how many digits did they want? 7?

haha yes good
