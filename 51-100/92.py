# more cutesy DP
limit = 10000000
fates = [0 for i in range(limit)]
fates[1] = 1
fates[89] = 89
for i in range(1, limit):
    stack = []
    cand = i
    while True:
        if cand < limit and (fates[cand] == 1 or fates[cand] == 89):
            for j in stack:
                if j < limit:
                    fates[j] = fates[cand]
            break
        else:
            stack.append(cand)
            cand = sum(map(lambda x: int(x) ** 2, list(str(cand))))

print sum(filter(lambda x: x == 89, fates)) / 89
