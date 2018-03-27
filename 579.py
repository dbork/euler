# the terrible cubes

## we should recurse on the upper corner
#def S(x):
#    if x == 1:
#        return 8
#    else:
#        # nah this doesn't work
#        #for sideLength in range(1, x):
#
#        # each cube is uniquely defined by
#        # its /opposing/ point
#
#        # but not all of them work...
#        # for squares, you need two of the same triangles
#        # for cubes, there's fewer degrees of freedom than
#        # you might think...they all have to have the same
#        # wedge, eg
#        # d^2 = a^2 + b^2 + c^2
#        # and then the side length is d
#        # and the cube is valid if and only if the distance
#        # to the opposite point squared is 3 times a fourth
#        # "wedge number" which we can procedurally generate
#
#        # the above aren't quiiite true. fixing an opposing
#        # point doesn't fix a cube, since you can rotate it
#        # about that axis. but it does partition cube
#        # space, in a way that's group-theoretically
#        # nice...i think into thirds, assuming a
#        # probably-pretty-reasonable hypothesis
#        # that each number is the hypoteneuse of at most one
#        # set of triangle numbers...
#        # but in case not we can also just generate the triangle
#        # numbers, which we should do anyways
#        
#        # as far as lattice points are concerned, should
#        # depend only on side length because you can
#        # cut and move the wedges around, and should be
#        # (floor(side length + 1))^3
#
#        # handle first corners, then edges, then sides, which
#        # have increasing numnbers of dofs. and assume
#        # wlog that each point we consider is the bottom-
#        # left of its cubes
#
#        # this makes the corner case easy, since there's
#        # only one:
#        # corner = sum_1^n (i+1)^3
#        # which has a closed form of degree at most 4
#        # s(x) = ax^4 + bx^3 + cx^2 + dx + e
#
#        # s(x+1) = s(x) + (x+1)^3
#        # a(x^4 + 4x^3 + 6x^2 + 4x + 1) + b(x^3 + 3x^2 + 3x + 1) + c(x^2 + 2x + 1) + d(x + 1) + e
#        # = ax^4 + bx^3 + cx^2 + dx + e + (x^3 + 3x^2 + 3x + 1)
#
#        # constant term: a + b + c + d = 1
#        # x term:        4a + 3b + 2c = 3
#        # x^2 term:      6a + 3b = 3
#        # x^3 term:      4a = 1
#
#        # a = 1/4, b = 1/2, c = 1/4, d = 0
#        # and for e, observe that s(2) needs to be 8, not 9.
#        # s(2) = 1/4(16) + 1/2(8) + 1/4(4) + e, e = -1
#
#        # test this formula:
#        #print float(x ** 4) / 4 + float(x ** 3) / 2 + float(x ** 2) / 4 - 1
#        #print sumCubes(x) - 1
#        # looks good to me
#        corner = sumCubesFast(x + 1)
#        #print corner
#
#        # we can also get the flat ones from the edges
#        # without too much trouble:
#        edgeFlats = sum([3 * sumCubesFast(x - i + 1) for i in range(1, x)])
#
#        # for the edges, you're lucky, and there's only one dof
#
#def sumCubesFast(x):
#    return float(x ** 4) / 4 + float(x ** 3) / 2 + float(x ** 2) / 4 - 1
#        
#def sumCubesSlow(x):
#    return sum(x ** 3 for x in range(x + 1))
#        
#print S(1)

import math

# ok, we're going to just start over tbh
def S(n):
    # we're going to build this up recursively using a DP table. here's the key
    # insight: DP[i] contains the number of the lattice points contained within
    # all of the cubes that are contained in a length-i lattice cube but that
    # ARE NOT contained within any of its lattice subcubes.
    DP = [0, 8]
    if n == 1:
        return 8

    # we need to manually calculate the triangle numbers less than n, for
    # reasons that will shortly become clear. we want to be able to index
    # into these efficiently given either the pair (a, b) or the hypoteneuse
    # c, so we'll use dicts
    triangles = {(a, b): int(math.sqrt(a ** 2 + b ** 2)) for a in range(1, n) \
                 for b in range(a, n) \
                 if math.sqrt(a ** 2 + b ** 2).is_integer()}
    reverseTriangles = {}

    for pair in triangles:
        if triangles[pair] not in reverseTriangles:
            reverseTriangles[triangles[pair]] = [pair]
        else:
            reverseTriangles[triangles[pair]].append(pair)

    #print reverseTriangles

    # helper function for later...
    def subtriangles(a, b, c):
        subs = set()
        for div in filter(lambda x: c % x == 0, range(1, c + 1)):
            if div in reverseTriangles:
                for triCand in reverseTriangles[div]:
                    smalla = triCand[0]
                    smallb = triCand[1]
                    if a == smalla * c / div and b == smallb * c / div:
                        subs.add(triCand)
        return subs

    print "triangle numbers calculated..."

    # precalculated squared R3 vector norms, for even later
    # this is way too slow though lol
    #normDict = {}
    #for i in range(1, n):
    #    for j in range(i, n):
    #        for k in range(j, n):
    #            normDict[(i, j, k)] = i ** 2 + j ** 2 + k ** 2

    #print normDict
    #print "norms calculated..."

    # next, calculate DP[x] recursively for x <= n. consider some lattice
    # cube C of side length x
    for x in range(2, n + 1):
        # first the hard part: calculating the lattice points contained within
        # the subcubes of C that aren't contained within any of its subcubes.
        
        # there is exactly one such cube that contains a corner of C -- C
        # itself.
        cornerLattice = (x + 1) ** 3

        # next, consider some face f of C; we're now going to
        # calculate the number of lattice points contained within subcubes
        # with one face incident to f (and do not contain a corner). observe
        # that the 6 sets of such subcubes are a) symmetric and b) disjoint,
        # since any cube with faces incident to more than one face of
        # C is either a subcube of C or contains a corner of C.
        # also, the incident face of each such subcube must touch
        # all four edges of C's face, as otherwise the subcube would be
        # contained within some other proper subcube of C. this means that
        # each set contains at most x - 1 subcubes, one for each
        # rotated lattice square that can be so inscribed in f.

        # we don't actually get this many, though -- since they have to be
        # lattice cubes, the side length must be an integer. so the cube is
        # only valid if j and x - j form two sides of a right triangle.
        # eg, the smallest x which has such a subcube is x = 7.
        faceLattice = 0
        for j in range(1, x / 2 + 1):
            if (j, x - j) in triangles:
                sideLength = triangles[(j, x - j)]
                # there are actually two such cubes per face, one for j
                # and one for x - j
                # notice we don't have to worry about the j = x - j case, since
                # this is never a valid side length

                # how many lattice points are in such a cube? in all cases,
                # this is equal to the number of lattice points in a flat
                # cube with side length i + 1 plus the number of lattice points
                # intersected by the sides of the cube
                internals = (sideLength - 1) ** 3

                # the sides parallel to f contain a number of lattice points
                # equal to those contained in a square of side length l - 1
                # plus one for each "subtriangle" (eg, for a 9/12/15 triangle,
                # there will be 3 lattice points, since "simplest form" is
                # 3/4/5). 
                subs = subtriangles(j, x - j, sideLength)
                print subs
                parallels = 2 * (sideLength - 1) ** 2 \
                          + 4 * (len(subs) - 1)

                # each nonparallel side will intersect a row of sideLength - 2
                # lattice points that haven't already been counted a number
                # of times equal to sideLength / sub
                slants = 4 * ((len(subs) - 1) * (sideLength - 2))

                # for each such subcube we found on this face, there are 12
                # total subcubes that need to be accounted for
                faceLattice += 12 * (slants + parallels)

        # next question: are there any large subcubes of C that don't have a
        # face incident with a face of C but do have a edge incident with a
        # face of C? if so, this edge /can't/ be incident to an edge of C

        # not sure. first i'm going to focus on the subcubes incident to
        # C at one point. assume WLOG that this point is on the bottom
        # face (eg z = 0). then what we need is three orthogonal, integer-
        # valued vectors with a certain norm, which is pretty restrictive.
        # that norm is also at most sqrt(3) * x
        maxNormSquared = 3 * x ** 2

        # the norms in question are sums of squares, so they have to be
        # positive integers lol

        print "x = " + str(x)
        print "cornerLattice = " + str(cornerLattice)
        print "faceLattice = " + str(faceLattice)
        # not done
        DP.append(cornerLattice)

    # finally, calculate the total number of lattice points by
    # adding all the subcube lattice points
    numSubcubes = [0] + [(x - i + 1) ** 3 for i in range(1, x + 1)]
    lattice = reduce(lambda a, b: a + b, \
              map(lambda y: DP[y] * numSubcubes[y], range(x + 1)))
    print DP
    return lattice

# geogebra is a good call for visualizing this
print S(100)
