# don't store anything!
# we can generate triangle number n + 1 from n by adding n + 1
# we can generate pentagonal number n + 1 from n by adding 3n + 1
# we can generate hexagonal number n + 1 from n by adding 4n + 1
# so just always increment the smallest one
# (i'm not actually sure this works in general...it seems to rely on
# the fact that incrementing the smallest one always minimizes the 
# spread, which might not be true if one of the sequences grows very fast...)

ti = 1
pi = 1
hi = 1

tri = 1
pent = 1
hexa = 1

while True:
    if tri == pent and tri == hexa:
        print tri
        if tri != 1 and tri != 40755:
            break

    smallest = min(tri, pent, hexa)
    if tri == smallest:
        tri += ti + 1
        ti += 1
    elif pent == smallest:
        pent += 3 * pi + 1 
        pi += 1
    else:
        hexa += 4 * hi + 1
        hi += 1
