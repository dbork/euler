# assume a <= b <= c, and start with a = b = c = p / 3. 
import math

# we're only using floats for integer- and half-integer values, so this
# method is true if and only if a float has an integer value
def isInt(f):
    return int(f) == int(f + 0.6)

sols = [0, 0, 0]
for p in range(3, 1000):
    solCount = 0
    a = float(p / 3)
    b = float(p / 3)
    c = float(p - (a + b))

    # observations: the sum a^2 + b^2 is minimized when a = b and, for any
    # given c, increases monotonically with the difference (b - a). thus,
    # for any c, there can be at most one valid (a. b) pair, and, as c
    # increases, we don't need to retry old pairs

    # also, by the triangle inequality, c can be at most p / 2
    if p == 120:
        print "a starts at " + str(a)
        print "b starts at " + str(b)
        print "c starts at " + str(c)
    while c < p / 2:
        if p == 120:
            print "a is now " + str(a)
            print "b is now " + str(b)
            print "c is now " + str(c)

        while a ** 2 + b ** 2 < c ** 2:
            if p == 120:
                print "a^2 + b^2 < c^2, increasing gap..."
            a -= 0.5
            b += 0.5
            if p == 120:
                print "a is now " + str(a)
                print "b is now " + str(b)
        
        if a ** 2 + b ** 2 == c ** 2 and isInt(a) and isInt(b):
            if p == 120:
                print "solution found"
            solCount += 1
        if p == 120:
            print "c increased"
            print "c is now " + str(c)
        a -= 0.5
        b -= 0.5
        c += 1

    sols.append(solCount)

print max(sols)
print sols.index(max(sols))
