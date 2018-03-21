# a + b + c = 1000
# square both sides
# a^2 + b^2 + c^2 + 2(ab + bc + ac) = 1000000
# 2c^2 + 2(ab + (1000 - c)c) = 1000000
# 2ab + 2000c = 1000000
# abc = 500000c - 1000c^2

# so first we loop over possible c, which satisfy
# c = 500 - (ab / 1000)
# which makes some sense, since you can't get a triangle with perimeter \leq
# 1000 if it has a hypoteneuse longer than 500
# and then we can just check that condition i guess

# the perimeter's also at most 3c though, so we can stick to the following c:
for c in range(334, 501):
    # this horrible list comprehension gets all the triangle numbers consistant
    # c with the c = 500 - (ab / 1000) condition and the perimeter sum condition
    l = [(a, b) for a in range(c) for b in range(c)\
            if abs(c - (500 - (float(a) * float(b) /1000))) < 10 ** -6\
            and a + b + c == 1000]
    
    print c
    print l
