# okay, let us think of some Facts About Concatenating Primes

# fact 1: obviously none of them can be 2 or 5 lmao
# fact 2: since none of them can be 0 mod 3, either all 5 must be 1 mod 3
#         or all 5 must be 2 mod 3 (with the singular exception of 3)

# what about other moduli?
# mod 5 gives no information, since multiplying by 10 sets it to 0
# mod 7? * 10 sends 1 -> 3, 2 -> 6, 3 -> 2, 4 -> 5, 5 -> 1, 6 -> 4
#        that yields forbidden combinations based on the length
#        of the primes, which is a tough thing to deal with systematically...
# mod 11 might be useful, since * 10 = * -1 mod 11. but ultimately idk if
#        even that is worth thinking too hard about...

# how else can we look at this? for each concatenated prime, one can
# figure out which primes it could have arisen from. eg for 109673, the
# only possible divisions are 109 673 and 10967 3 by inspection, and
# in fact 10967 isn't prime anyways. this could be interpreted as an edge 
# in a graph that has a 5-cycle iff there is a corresponding 5-set. 

# but minimality's hard to test... amd also this seems brute-forcey, which
# makes me kinda worried it's not going to be enough. oh well, let's go
# ahead with it anyways and see what happens lol
import sys
sys.path.append("..")
import math
import primes

limit = 10000000
cliqueSize = 5
primesList = primes.getPrimes(limit, "log")
edges = {}
filteredPrimes = filter(lambda x: x != 0, primesList)

for prime in filteredPrimes[4:]:
        # heuristic progress-report clause
        if math.log(prime, 2) - int(math.log(prime, 2)) \
                                                  < 1.0 / math.sqrt(prime):
                print "adding edges from " + str(prime)

        primeString = str(prime)
        #print "next prime: " + str(prime)

        for divider in range(1, len(primeString)):
                left = primeString[:divider]
                right = primeString[divider:]
                reverse = int(right + left)

                # if right begins with a 0, we can ignore this division, as
                # no concatenation will result in it
                if str(right)[0] == '0':
                        continue

                left = int(left)
                right = int(right)

                # we only want to add each edge once
                if left > right:
                        continue

                # to add this edge, we both need the components to be prime and
                # for the reversed concatenation to also be prime
                if primesList[left] and primesList[right] and primesList[reverse]:
                        #print "adding an edge..."
                        #print left
                        #print right
                        if left not in edges:
                                edges[left] = [right]
                        else:
                                edges[left].append(right)

                        if right not in edges:
                                edges[right] = [left]
                        else:
                                edges[right].append(left)

print "graph calculated..."

# helper function for the clique checker
def cycleToClique(edges, cycle):
        for i in range(len(cycle)):
                # the cycle checker already checks all the adjacencies, so we just
                # need to check the crossing-edges here
                for j in range(i + 2, len(cycle)):
                        if cycle[j] not in edges[cycle[i]]:
                                return False

        return True

# now we need to write a clique checker
# this assumes length is odd, but that's fine
# (was originally a cycle checker, but that's not actually the right condition)
def getCliques(edges, length):
        cycles = []

        for prime in filteredPrimes:
                # heuristic progress-report clause
                if math.log(prime, 2) - int(math.log(prime, 2)) \
                                                          < 1.0 / math.sqrt(prime):
                        print "getting cliques containing " + str(prime)         

                paths = [[] for i in range(length / 2 + 1)]
                paths[0] = [[prime]]

                for i in range(1, len(paths)):
                        for prevPath in paths[i - 1]:
                                if prevPath[-1] not in edges:
                                        continue

                                for neigh in edges[prevPath[-1]]:
                                        paths[i] += [prevPath + [neigh]]

                # now we have to close the cycle
                ends = {path[-1]: path for path in paths[-1]}

                for end in ends.keys():
                        for neigh in edges[end]:
                                if end < neigh and neigh in ends.keys():
                                        cycle = [ends[end] + list(reversed(ends[neigh]))][0][:-1]
                                        # only want to add each cycle once and only want to
                                        # add cycles with no repeats

                                        # ed: and also only the ones with all their crossing-edges
                                        if cycle[0] == min(cycle) \
                                                        and len(set(cycle)) == length \
                                                                and cycleToClique(edges, cycle):
                                                cycles.append(cycle)

        return cycles

cliques = getCliques(edges, cliqueSize)
print cliques
cliques = list(sorted(cliques, key=lambda x: sum(x)))
#print cycleToClique(edges, [3, 7, 109, 673])
print cliques[0]
print sum(cliques[0])

# if this is too slow (and rn it is), we can build them up from triangles

