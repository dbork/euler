# we'll start by listing all of the abundant numbers less than 28123
divSums = [0 for i in range(28124)]
for j in range(1, 28124/2):
    #print j
    jMults = [0] * (2 * j) + [j * int(not i % j) for i in range(28124 - j)]
    divSums = [divSums[k] + jMults[k] for k in range(len(divSums))]
#print divSums
abundants = list(filter(lambda x: divSums[x] > x, range(28124)))
#print abundants
# set comprehensions?
abunSums = {x + y for x in abundants for y in abundants}
#print abunSums
print sum([x for x in range(28124) if x not in abunSums])
