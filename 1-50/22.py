f = open('p022_names.txt')
ordConst = 64
names = f.readline().strip('\"')
names = sorted(names.split('\",\"'))
scoreSum = sum(map(lambda x: (names.index(x) + 1) * sum(map(lambda y: ord(y) - ordConst, x)), names))
#print names[0]
#print sum(map(lambda y: ord(y) - ordConst, "COLIN"))
f.close()
print scoreSum
