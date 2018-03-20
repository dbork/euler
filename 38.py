# since one of them starts with a 9, so does the largest one. so we only
# have to check multiples of things that start with 9, lmao
best = 918273645

# also, what if the multiplicand x was 2 digits long? we know it starts with
# 9, so 2 * x is 3 digits long, as is 3 * x and 4 * x. but that's a contra-
# diction, since the concatenated product must be exactly 9 digits long.
# similarly, if x had 3 digits, 2 * x would have 4, and we have the same
# contradiction. so we only need to check x's with 4 digits that start with 9.

# so that gives that the concatenated product is 9bcd18ghi for some b, c, d,
# g, h, i, since we need to not have 19 as the first two digits of 2 * x.
# then we can keep choosing digits greedily, since the first multiple being
# 1 * x means we can never beat a greedily-selected digit. the largest
# eligible b is 3, since 8 and 9 are both off-limits for g. the largest
# eligible c is not 7, since that gives g = 7 as well. but c = 6 works fine.
# this gives 936d1872i. but the last two need to be 5 and 4, which is
# impossible and the reason greed doesn't work, ok

# so we can relax either the b = 3 or c = 6 constraints to fix this. we ofc
# prefer the latter, and also can't relax a = 9 and still beat the 9 *
# (1, 2, 3, 4, 5) product (which it's worth test-submitting just to be sure).
# we can't make c = 5 though, as we then have h = 0 or 1. indeed, c != 4 for
# the same reason. how about 2? that gives 932d1864i. then d = 7 works
# perfectly, giving 932718654. let's try that?

# hahaha it worked omg! yes good. pencil and paper count = 1 :)
print 932718654
