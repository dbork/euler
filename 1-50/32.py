# we're going to use itertools for this, so let it be known that i more or less
# read the whole itertools man page, as per Law.
import itertools as it

prods = set()
for perm in it.permutations(map(str, range(1, 10))):
    # we also need a little more than that, since we don't have time to
    # do any really significant computations in here
    # how long can prod be? not 3 digits or fewer, since that must be a product
    # of a 3 digit number with another 3 digit number, or worse.
    # 4 is fine, eg the example. 5 digits must be the product of two 2-digits,
    # which is impossible. so prod can always be the last 4
    prod = int(''.join(perm[-4:]))

    # now what do we know? the result can clearly be a 2-digit times a 3-digit,
    # as per the example. it can also be a 1-digit times a 4-digit in theory,
    # but that one-digit multiplication can't be 1 * something because digits
    # will be repeated, and if it's n * something for n > 1, there are a lot of
    # constraints. still, it's possible to imagine something like
    # 3 * 1489 = 4467, which is pretty close, working. so that means we have
    # to try exactly two positions of the * operator
    multiplicand1 = int(perm[0])
    multiplier1 = int(''.join(perm[1:5]))
    multiplicand2 = int(''.join(perm[0:2]))
    multiplier2 = int(''.join(perm[2:5]))

    if multiplicand1 * multiplier1 == prod:
        #print str(multiplicand1) + " * " + str(multiplier1) + " = " + str(prod)
        prods.add(prod)

    if multiplicand2 * multiplier2 == prod:
        #print str(multiplicand2) + " * " + str(multiplier2) + " = " + str(prod)
        prods.add(prod)

print sum(prods)
