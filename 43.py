# there are a fair few 10-digit pandigitals, so how can we avoid looping
# over all of them?

# let a pandigital be abcdefghij. then let's go through the properties:
#   2 | bcd if and only if d is in {0, 2, 4, 6, 8}, fine
#   3 | cde if and only if c + d + e = 0 mod 3, which at least cuts this
#       down by another factor of 3
#   5 | def if and only if f is in {0, 5}
# and then the rest of the constraints aren't number-theoretically nice to
# my admittedly limited knowledge...but can still be used to cut down the
# search space by a factor of p for the given prime p.

# so one way to solve this quickly-in-practice is to recurse over the
# constraints. eg for each prime get a list of all the three-digit multiples
# (ie between 010 and 999) with unique digits:
def str3(x):
    s = str(x)
    if len(s) == 2:
        s = '0' + s
    return s

def threeUniqueDigits(x):
    s = str3(x)
    if len(s) < 2 or len(s) > 3:
        return False
    return s[0] not in s[1:] and s[1] != s[2]

primes = [2, 3, 5, 7, 11, 13, 17]
primeMults = [[str3(x * p) for x in range(1, 1000 / p) \
              if threeUniqueDigits(x * p)] for p in primes]

# first, tail-recurse over the constraints to determine the last 9 digits.
# then, the first digit is uniquely determined.
pans = []

def constrainSearch(constraintNum, digits):
    # base case
    if constraintNum == len(primes):
        # add the last remaining digit to the front of the number
        digits = filter(lambda x: x not in digits, map(str, range(10))) + digits
        pans.append(int(''.join(digits)))

    # else recurse
    else:
        for candidate in primeMults[constraintNum]:
            if constraintNum == 0:
                constrainSearch(constraintNum + 1, list(candidate))
            elif candidate[0] == digits[-2] and candidate[1] == digits[-1] \
                and candidate[2] not in digits:
                constrainSearch(constraintNum + 1, digits + list(candidate[2]))

constrainSearch(0, [])
print pans
print sum(pans)
