# lmao python
#print 28433 * 2 ** 7830457 + 1
# wow, looks like we actually found the limits of what python ints can
# do effectively. fiiiine i'll like actually try
bigPower = 7830457
last10 = 2
power = 1
last10prod = 1
while power <= bigPower:
    if power <= bigPower / 2:
        power *= 2
        last10 = (last10 ** 2) % (10 ** 10)
    else:
        last10prod = (last10prod * last10) % (10 ** 10)
        bigPower -= power
        power = 1
        last10 = 2

print (28433 * last10prod + 1) % (10 ** 10)
