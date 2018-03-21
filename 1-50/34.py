# they all have to be less than 2540160 = 7 * 9!, since any larger number
# will require more digits to be factorialized to equal it than are in
# its own digit representation (eg every 8-digit number is more than 8 * 9!)
import math

print -3 + sum([x for x in range(2540160) if list(str(x)) \
        == list(str(sum(map(lambda y: math.factorial(int(y)), list(str(x))))))]) 

