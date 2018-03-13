# sad-person sieve
import sys
import math

primesList = range(2, 20000)
index = 1
while index < len(primesList):
    #print index
    #print "considering " + str(primesList[index]) + " at index " + str(index)
    #print primesList[:index]
    for j in primesList[:index]:
        #print "j: " + str(j)
        if primesList[index] % j == 0:
            #print "removing " + str(primesList[index])

            # goldbach-specific test
            if primesList[index] % 2 == 1:
                for prime in primesList[:index]:
                    #print prime
                    #print '%s'%(math.fabs(math.sqrt((primesList[index] - prime) / 2) - int(math.sqrt((primesList[index] - prime) / 2))))
                    if math.fabs(math.sqrt((primesList[index] - prime) / 2) - int(math.sqrt((primesList[index] - prime) / 2))) < math.pow(10, -10):
                        break
                else:
                    print primesList[index]
                    exit()
                
            primesList.pop(index)
            #print primesList
            break
    else:
        #print str(primesList[index]) + " is prime"
        index += 1

#print len(primesList)
#print primesList[10000]
