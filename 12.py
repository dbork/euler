# for each prime p, we sum 1 + 2 + ... + p-1 + p mod p, and it's
# a divisor if and only if the result is zero

# this is both not a smart way of doing it and actively doesn't work:

#divs = [1] * 1000
#for divisor in range(2, 10000):
#    modulus = 0
#    modSum = 0
#    for index in range(len(divs)):
#        modulus = (modulus + 1) % divisor
#        modSum = (modSum + modulus) % divisor
#        if modSum == 0:
#            divs[index] += 1
#
#print divs

# okay here's the next attempt
import operator as op

# need to hard-code the base case to dodge issues with the check
#modList = [1, 1, 0]
#div = 3
#triangle = 3
#maxSoFar = 0
#print div
#print triangle
#print modDict.items()
#print map(lambda x: int(not(x[1])), modDict.items())
#print reduce(lambda x, y: x + y, map(lambda x: int(not(x[1])), modDict.items()))
# this check counts the divisors of the current triangle number
#while reduce(lambda x, y: x + y, map(lambda x: int(not(x)), modList)) < 500:
#    if reduce(lambda x, y: x + y, map(lambda x: int(not(x)), modList)) > maxSoFar:
#        maxSoFar = reduce(lambda x, y: x + y, map(lambda x: int(not(x)), modList)) 
#        print 'div: ' + str(div)
#        print 'triangle: ' + str(triangle)
#        print "max so far: " + str(maxSoFar)
    #print div
    #print triangle
    #print reduce(lambda x, y: x + y, map(lambda x: int(not(x[1])), modDict.items()))

#    for item in range(len(modList)):
#        modList[item] = (modList[item] + div) % (item + 1)
#    for j in range(triangle + 1, triangle + div + 1):
#        modList.append((triangle + div) % j)
#    triangle += div
#    div += 1

    #print modDict
#print modDict
#print triangle

# unfortunately, that's also too slow to be practical
# which means i have to, like, think about this lol

# ok had a few insights by looking for patterns and using my notebook,
# which is now the official theorizing-place. let's try again

modList = [0, 0, 1, 0, 4]
divsList = [1, 2, 2, 3] 
j = 3
maxSoFar = 0
triDiv = 0

while triDiv < 500:

    if j % 2 == 1:
        triDiv = divsList[j - 1] * divsList[(j - 1) / 2]
    else:
        triDiv = divsList[j] * divsList[(j / 2) - 1]

    if triDiv > maxSoFar:
        maxSoFar = triDiv
        print "triangle #: " + str(j)
        print "which is " + str(sum(range(j + 1)))
        print "max so far: " + str(maxSoFar)
        #print "triDiv = " + str(triDiv)
        #print "modList = " + str(modList)
        #print "divList = " + str(divsList)

    for item in range(len(modList)):
        modList[item] = (modList[item] + 1) % (item + 1)
    modList.append(j + 2)
    divsList.append(reduce(lambda x, y: x + y, map(lambda x: int(not(x)), modList)))\

    j = j + 1
