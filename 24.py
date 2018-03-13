# 10! total perms
import math

# awkward off-by-one error
permNum = 999999
perm = [0] * 10
choices = range(10)
for i in range(10):
    choice = permNum / math.factorial(10 - i - 1)
    perm[i] = choices.pop(choice)
    permNum = permNum % math.factorial(10 - i - 1)
print ''.join(map(lambda x: str(x), perm))
