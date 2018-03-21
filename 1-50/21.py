# stolen divisorSum code from 21.py
divSums = [0 for i in range(10001)]
for j in range(1, 5001):
    #print j
    jMults = [0] * (2 * j) + [j * int(not i % j) for i in range(28124 - j)]
    divSums = [divSums[k] + jMults[k] for k in range(len(divSums))]
#print divSums
amics = [x for x in range(10001) for y in range(10001) \
         if divSums[x] == y and divSums[y] == x and y != x]
#print amics
print sum(amics)
