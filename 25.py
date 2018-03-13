# lol
import math

i = 2
fibs = (1, 1)
#print fibs

while True:
    i += 1
    fibs = (fibs[0] + fibs[1], fibs[0])
    if math.log(fibs[0], 10) > 999:
        print i
        break
