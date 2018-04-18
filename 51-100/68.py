# ok first up, what totals are possible?
# for the 3-gon, we know that 3(T) = 2 sum(triangle) + sum(outer)
# which is a weighted average of the three inner and three outer ones
# the minimum inner sum is 6, which gives outer sum 21 - 6 = 15
# and weighted average 6 * 2/3 + 15 * 1/3 = 9
# the max inner sum is 15, with outer sum 6, which gives 12
# this is the given range, which is a good sign

# for the 5-gon, we have a restriction, namely that 10 can't be in the inner
# pentagon.
# the minimum inner pent possible is then 15, with outer ring 40,
# which gives sum 10 + 40/3. that's not an integer, so the actual min
# possible sum is 24
# the max inner pent is 35 (9 + 8 + 7 + 6 + 5), with outer ring 20,
# which gives sum 30, which conveniently /is/ an integer

# so how do we maximize the string? they're ordered increasingly by their
# /smallest/ outer ring element, then by the sum, since we can flip the
# chirality to get the second-largest element in the leg ending in the
# smallest outer ring element adjacent to said element (i think?)

# anyway, that says to me that ideally we want to get as close to 40 in the
# outer ring sum as possible. 40 itself doesn't work, since it doesn't
# give an integer solution to the sum, but 38 gives 2/3 * 17 + 1/3 * 38
# = 72 / 3 = 24, with 38 equaling 10 + 9 + 8 + 6 + 5. is such a ring
# actually possible?

# ...no, because the sum calcs for the pentagon are wrong lol. it's
# actually 2/5 * inner + 1/5 * outer haha. but that means
# 2/5 * 15 + 1/5 * 40 = 14 is actually an integer, with
# outer ring 10 + 9 + 8 + 7 + 6, which is the best possible. is /that/
# possible?

# we want 6 next to 5 if we can get it, which gives 6 5 3 as the first
# leg. then 7 2 5 is a good idea, and 8 4 2, 9 4 1, which leaves as
# the last edge 10 3 1, awesome.

# then reading off the resultant string gives
print 6531031914842725
