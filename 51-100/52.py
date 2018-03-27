# some observations: digit 1 must be 1. sets are good. must have at least 3
# digits, for what that's worth. must be 0 mod 3. must contain at least 6
# distinct digits, since the first digit doesn't repeat. second digit must
# be less than 7, since 17 * 6 = 102
def digitCount(x):
    return {i: list(str(x)).count(i) for i in list(str(x))}

l = 6
flag = False
while not flag:
    lower = int('1' + '0' * (l - 2) + '2')
    upper = int('1' + '7' + '0' * (l - 3) + '1')
    cands = filter(lambda x: len(set(list(str(x)))) >= 6, \
                   range(lower, upper, 3))

    for cand in cands:
        mults = [digitCount(j * cand) for j in range(1, 7)]
        if mults[0] == mults[1] and mults[0] == mults[2] \
                and mults[0] == mults[3] and mults[0] == mults[4] \
                and mults[0] == mults[5]:
            print cand
            flag = True
