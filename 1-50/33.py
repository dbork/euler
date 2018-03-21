# 49 / 98 = 4 / 8 is one, fine. there are few enough of them that we can just
# iterate and it'll be fine i guess...
denoms = set()
for i in map(str, range(1, 10)):
    for j in map(str, range(1, 10)):
        for k in map(str, range(1, 10)):
            if float(i + j) / float(j + k) == float(i) / float(k) and i != k:
                denoms.add(int(j + k))
                print i + j + '/' + j + k + ' = ' + i + '/' + k

