# not sure i see a super clean way to do this
# so uh let's make a dictionary of count strings i guess
# whereby count strings i mean the equivalent, easier thing that is
# the list of digits in roted order
i = 0
digits = []
cubeDigits = {}
while True:
    digitString = ''.join(sorted(list(str(i ** 3))))
    digits.append(digitString)
    if digitString in cubeDigits:
        if cubeDigits[digitString] == 4:
            print digits.index(digitString) ** 3
            break
        else:
            cubeDigits[digitString] += 1
    else:
        cubeDigits[digitString] = 1
    i += 1
