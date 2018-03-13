# oh man, this one is dictionaries
import operator

collatz = {'1': 0}

for i in range(2, 1000000):
    num = i
    count = 0
    stack = []
    
    while str(num) not in collatz:
        stack.append(num)
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1

    for j in range(count):
        collatz[str(list.pop(stack))] = collatz[str(num)] + j + 1

print sorted(collatz.items(), key=operator.itemgetter(1), reverse=True)[0]
