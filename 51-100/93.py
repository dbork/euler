# ok we kinda have an insight...namely, parens are a proxy for recursive
# structure. looks like a hash map? and we only have to try 10 ** 4
# 4-digit combinations, that's doable. gr8

# i'd also say it's fair to assume the result doesn't have 0 in it,
# since 0 is super useless for making distinct things
import itertools as it
limit = 5

combs = {'1': {1}, '2': {2}, '3': {3}, '4': {4}, '5': {5}, '6': {6}, '7': {7},\
         '8': {8}, '9': {9}}

for length in range(2, limit):
    for digitSet in it.combinations('123456789', length):
        targets = set()
        # we have to recurse on each digit in digitSet, since each of them
        # can have the outermost parenthetical priority...
        for digit in digitSet:
            # now we can place this digit at any position in the expression,
            # and recurse on both sides...
            others = list(digitSet)
            others.remove(digit)
            digit = int(digit)
    
            # first, handle the cases where this digit is the first or last
            # manually, to avoid weirdness with zero
            for comb in combs[''.join(others)]:
                if comb % digit == 0:
                    targets.add(comb / digit)
                if comb != 0 and digit % comb == 0:
                    targets.add(digit / comb)
                
                # subexpressions can be negative. well, maybe there's a way
                # around needing to record this, but i don't want to think
                # about it lol
                targets.add(comb - digit)
                targets.add(digit - comb)
                
                targets = targets.union({digit + comb, digit * comb})

            # now, handle the other cases...
            for digitPos in range(1, length - 1):
                # first, loop over all possible left-half digit subsets...
                for leftSide in it.combinations(''.join(others), digitPos):
                    left = list(leftSide)
                    # next, get the right-side digits...
                    right = list(digitSet)
                    right.remove(str(digit))
                    for i in left:
                        if i in right:
                            right.remove(i)

                    # now, digit is between the left side and the right side
                    leftCombs = combs[''.join(left)]
                    rightCombs = combs[''.join(right)]

                    # next, try every combination
                    for l in leftCombs:
                        for r in rightCombs:
                            # first, combine the left side with digit first
                            validL = [l + digit, l * digit]
                            #if l - digit > 0:
                            validL.append(l - digit)
                            if l % digit == 0: #and l > digit:
                                validL.append(l / digit)
                    
                            # now try combining the result with r
                            valids = [v + r for v in validL]
                            valids += [v * r for v in validL]
                            valids += [v - r for v in validL if v - r > 0]
                            valids += [v / r for v in validL if r != 0 \
                                                             if v % r == 0]

                            targets = targets.union(set(valids))

                            # now, try the other way
                            validR = [digit + r, digit * r]
                            #if digit - r > 0:
                            validR.append(r - digit)
                            if r != 0 and digit % r == 0: #and digit > r:
                                validR.append(r / digit)

                            valids = [l + v for v in validR]
                            valids += [l * v for v in validR]
                            valids += [l - v for v in validR if l - v > 0]
                            valids += [l / v for v in validR if v != 0 \
                                                             if l % v == 0]

                            targets = targets.union(set(valids))

        combs[''.join(digitSet)] = targets

positives = {a: filter(lambda x: x > 0, combs[a]) for a in combs}
ns = {b: min(filter(lambda y: y not in positives[b], \
             range(1, len(positives[b]) + 2))) for b in positives}
#lengths = {b: len(positives[b]) for b in positives}
print sorted(ns, key=lambda c: ns[c])
