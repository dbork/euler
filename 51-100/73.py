# this is hard to do with totients, the overview for 72 says
# let us determine if that is indeed the case :P
# it sure looks like it at first blush...

# observation 1: there are as many between 1/3 and 1/2 as between 1/2 and 2/3,
# since, iff n/d is unique, eg n is relatively prime to d, d-n is also
# relatively prime to d, as otherwise their sum mod some divisor of d would not
# be 0, as required. so that's a start... and, by the same logic, the number
# between 0 and 1/3 as between 2/3 and 1.

# so we can divide the set of unique fractions into 
# [1st third] + 1/3 + [3rd sixth] + 1/2 + [4th sixth] + 2/3 + [3rd third]
# where we know |[1st third]| = |[3rd third]| and |[3rd sixth]| = |[4th sixth]|

# the million-dollar question then is
# does |[1st third]| = 2 * |[3rd sixth]|?
# it does in the given example. is there any reason for this?
# it's not the same one as above... we can't naively reflect about 1/3 the way
# we did about 1/2 without multiplying by 3/2 first, which might work
# asymptotically but not wrt to a given upper bound on d...

# it works for eg d = 7, since the pattern of sevenths in the first third
# is [3/21, 6/21] (plus the interval lower bound) and the pattern in
# the second third is [2/21, 5/21], which is a translation of 1/21 from
# the previous one... or, in logic that actually makes sense, because
# totient(7) = 6 and, if they're evenly distributed, there have to be
# two in each bucket lol. so 7's a bad example... for fifths, eg, it doesn't
# hold, but that's made up for by some other asymmetry... so probs coincidence

# ok, here's something we do know: since they're symmetric about 1/2,
# we know that for any prime d such that d-1 = 0 mod 3, they're evenly
# distributed. for d-1 = 1 mod 3, the extra is in the middle third, and for
# d-1 = 2 mod 3, the extras are in the outer thirds (were that possible lol)
# which means it's true if you count repeats too (at least up to +- 1) and
# assume 1/3 is in the first bucket and 2/3 in the last

# wait, what am i doing, i should be doing this mod 6 lmao. #justmod6things
# in this case, there are 6 buckets excluding endpoints... or something...

# uh, anyways...
import sys
sys.path.append("..")
import totients as tot
limit = 12

# the remaining unique fractions between 1/2 and 1/3 should equal half of the
# totient sum minus the "first third", which i've modified the totient
# sieve to calculate. not mathy, but should work
total = sum(tot.getTotients(limit)[2:])
firstThird = sum(tot.getTruncatedTotients(limit, 3))
print (total - 1) / 2 - firstThird

print tot.getTotients(limit)
print tot.getTruncatedTotients(limit, 3)
