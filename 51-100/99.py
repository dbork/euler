# man why am i in such a weird mood
# well, that's perfect for exponentiation i guess
import math

bases = []
exponents = []

f = open("p099_base_exp.txt")
for line in f:
    parsed = line.rstrip().split(",")
    bases.append(int(parsed[0]))
    exponents.append(int(parsed[1]))
f.close()

# reasonably, these numbers are big enough that we can't solve this just by
# asking python nicely lol

# but, duh, we can just take the log
logs = [exponents[i] * math.log(bases[i]) for i in range(len(bases))]
print logs.index(max(logs)) + 1
