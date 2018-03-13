# sneaky fib DP
# every third term is even and equal to 4(F_(n-1)) + F_(n-2)

sum = 2
current = 8
prev = 2

while current < 4000000:
    sum += current
    prev += 4 * current
    prev, current = current, prev
    #print "sum = " + str(sum)
    #print "current = " + str(current)

print sum

# ps that was really wasteful, i'm sure this has a closed-form,
# but it's an irritating geometric series sum of sums and i
# don't really feel like deriving it rn lol
