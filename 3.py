import math as m
import sys

num = 600851475143
facs = [num]

# lol, lists are bools
# this would be better with a heap but i don't care lol
while facs:
    #print facs
    fac = facs.pop(0)
    i = int(m.sqrt(fac))
    while i > 1:
        if fac % i == 0:
            facs.append(fac / i)
            facs.append(i)
            facs.sort(reverse = True)
            break
        i -= 1

        if i == 1:
            print fac
            exit()
    
    
