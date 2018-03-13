# the terrible cubes

# we should recurse on the upper corner
def S(x):
    if x == 1:
        return 8
    else:
        # nah this doesn't work
        #for sideLength in range(1, x):

        # each cube is uniquely defined by
        # its /opposing/ point

        # but not all of them work...
        # for squares, you need two of the same triangles
        # for cubes, there's fewer degrees of freedom than
        # you might think...they all have to have the same
        # wedge, eg
        # d^2 = a^2 + b^2 + c^2
        # and then the side length is d
        # and the cube is valid if and only if the distance
        # to the opposite point squared is 3 times a fourth
        # "wedge number" which we can procedurally generate

        # the above aren't quiiite true. fixing an opposing
        # point doesn't fix a cube, since you can rotate it
        # about that axis. but it does partition cube
        # space, in a way that's group-theoretically
        # nice...i think into thirds, assuming a
        # probably-pretty-reasonable hypothesis
        # that each number is the hypoteneuse of at most one
        # set of triangle numbers...
        # but in case not we can also just generate the triangle
        # numbers, which we should do anyways
        
        # as far as lattice points are concerned, should
        # depend only on side length because you can
        # cut and move the wedges around, and should be
        # (floor(side length + 1))^3

        # handle first corners, then edges, then sides, which
        # have increasing numnbers of dofs. and assume
        # wlog that each point we consider is the bottom-
        # left of its cubes

        # this makes the corner case easy, since there's
        # only one:
        # corner = sum_1^n (i+1)^3
        # which has a closed form of degree at most 4
        # s(x) = ax^4 + bx^3 + cx^2 + dx + e

        # s(x+1) = s(x) + (x+1)^3
        # a(x^4 + 4x^3 + 6x^2 + 4x + 1) + b(x^3 + 3x^2 + 3x + 1) + c(x^2 + 2x + 1) + d(x + 1) + e
        # = ax^4 + bx^3 + cx^2 + dx + e + (x^3 + 3x^2 + 3x + 1)

        # constant term: a + b + c + d = 1
        # x term:        4a + 3b + 2c = 3
        # x^2 term:      6a + 3b = 3
        # x^3 term:      4a = 1

        # a = 1/4, b = 1/2, c = 1/4, d = 0
        # and for e, observe that s(2) needs to be 8, not 9.
        # s(2) = 1/4(16) + 1/2(8) + 1/4(4) + e, e = -1

        # test this formula:
        #print float(x ** 4) / 4 + float(x ** 3) / 2 + float(x ** 2) / 4 - 1
        #print sumCubes(x) - 1
        # looks good to me
        corner = sumCubesFast(x + 1)
        #print corner

        # we can also get the flat ones from the edges
        # without too much trouble:
        edgeFlats = sum([3 * sumCubesFast(x - i + 1) for i in range(1, x)])

        # for the edges, you're lucky, and there's only one dof

def sumCubesFast(x):
    return float(x ** 4) / 4 + float(x ** 3) / 2 + float(x ** 2) / 4 - 1
        
def sumCubesSlow(x):
    return sum(x ** 3 for x in range(x + 1))
        
print S(1)
