# sad-person sieve

primesList = range(2, 200000)
index = 1
while index < len(primesList):
    #print index
    #print "considering " + str(primesList[index]) + " at index " + str(index)
    #print primesList[:index]
    for j in primesList[:index]:
        #print "j: " + str(j)
        if primesList[index] % j == 0:
            #print "removing " + str(primesList[index])
            primesList.pop(index)
            #print primesList
            break
    else:
        #print str(primesList[index]) + " is prime"
        index += 1

#print len(primesList)
print primesList[10000]
