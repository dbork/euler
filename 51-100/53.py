# lol just count the smaller ones and subrtract from the total
# i'm going to just do this manually honestly
# we know all the ones for n < 23 are smaller
smaller = 23 * 11

# for 23, we know the first 9 and last 10 (note the asymmetry) are smaller
# the first n for which n choose 9 is greater is 24
smaller += 19

# the first n for which n choose 8 is greater is 25
smaller += 17

# for n choose 7, it is 28
smaller += 15 * 3

# for n choose 6, it is 33
smaller += 13 * 5

#for n choose 5, it is 44
smaller += 11 * 11

# for n choose 4, it is 72
smaller += 9 * 28

# and 100 choose 3 is smaller
smaller += 7 * 29

# the total should be the sum from 1 to 100 of n = 5050
print 5050 - smaller
