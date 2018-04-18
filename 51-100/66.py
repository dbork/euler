# ok what the heck can we do with this thing
# x^2 - Dy^2 = 1
# (x + sqrt(D)y)(x - sqrt(D)y) = 1
# x + sqrt(D)y = 1/(x - sqrt(D)y)
#              = (x + sqrt(D)y)/(x^2 - Dy^2)
# well that's useless

# try again
# x^2 \in {0, 1, 4, 5, 6, 9} mod 10

# more trying
# fact 1: x has to be in (-1, 1) mod D, cool
# so that means x = aD +- 1 for some a
# a^2D^2 +- 2aD - Dy^2 = 0
# y^2 = a^2D +- 2

# ...OR D can already be one less than a perfect square, eg 15
# but then that's super easy, min x is just sqrt(D + 1)

# hmm observe for 13
# 12^2 - 1 = 11*13
# 14^2 - 1 = 13*15
# 25^2 - 1 = 24*26 = 13*48
# 27^2 - 1 = 26*28 = 13*56

# eg 13 - 2, 13 + 2, 4(13) - 4, 4(13) + 4, 9(13) - 6, 9(13) + 6...

# and 649^2 - 1 = 648 * 650 = 13 * 25 * 2 * 2 * 18 * 18
# then 651^2 - 1 = 650 * 652
# so 180^2 = 50^2(13) - 100

# anyway, we're looking for perfect square solutions to 13a^2 +- 2a = x
# every time a increments, the positive solution increases by 26a + 15
# and the negative by 26a + 11

# why does 50 work? 50(13 * 50 - 2) = 50(12 * 50 + 48) = 50(12 * 54)...

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# not sure i'm going to think of anything better than smashing it
import math

limit = 300
minx = [0 for i in range(limit + 1)]

for D in range(2, limit + 1):
    # perfect squares have no solutions
    if D in [i ** 2 for i in range(int(math.sqrt(limit)) + 1)]:
        #print(D)
        continue
    if D % 10 == 0:
        print(D)

    if math.sqrt(D + 1).is_integer():
        minx[D] = int(math.sqrt(D + 1))
        continue
    x = 0
    x2 = 1
    y = 0
    Dy2 = 0
        
    mods = [k ** 2 % D for k in range(D)]
    rootsOfUnity = [j for j in range(D) if mods[j] == 1]
    #print(D)
    #print(rootsOfUnity)
    
    while True:
        cands = [D * x + a for a in rootsOfUnity]
        #print(cands)

        prevCand = D * x - 1
        for cand in cands:

            # go from the last candidate to this one
            x2 += (cand - prevCand) ** 2 + 2 * prevCand * (cand - prevCand)
            #print(x2)

            if x2 == 1:
                continue

            while Dy2 < x2 - 1:
                y += 1
                Dy2 += D * (2 * y - 1)

            if Dy2 == x2 - 1:
                minx[D] = cand
                break

            prevCand = cand

        if minx[D] != 0:
            break

        x += 1

        # uhhhh why are some of them not working
        if x > D ** 2:
            print(str(D) + " timeout")
            minx[D] = float('inf')
            break

print(minx)
print(minx.index(max(minx))) 
