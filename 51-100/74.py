# more DP hooray
import math

limit = 1000000
chainTarget = 60
chain = [2] + [1] + [0 for i in range(limit - 2)]
stack = []

for start in range(2, limit):
    cand = start
    if chain[start] != 0:
        continue
    else:
        while cand not in stack and (cand >= limit or chain[cand] == 0): 
            stack.append(cand)
            cand = sum(map(math.factorial, map(int, list(str(cand)))))

        if cand in stack:
            loopLength = len(stack) - stack.index(cand)
            length = loopLength
        else:
            length = chain[cand] + 1

        while len(stack) > 0:
            last = stack.pop()
            if last < limit:
                chain[last] = length
            if cand not in stack:
                length += 1

print len(filter(lambda x: x == 60, chain))
