# this is the first one that i think wants numpy
import numpy as np

# writing this out as a system of equations...
# abc * def = ad * 10^5 + (ae + bd) * 10^4 + ...
# wait this sucks :(

# ok i'm a lazy boi
dim = 999
range = 0
pal = 0

# this condition makes sure we don't fill in too much
# of the metaphorical dp table...
while (dim - range / 2) ^ 2 > pal:
    i = dim - range
    j = dim

    # ...which we fill in by looping diagonally
    while i <= dim:
        prod = i * j
        arr = np.array(list(str(prod)), dtype=int)
        
        # palindrome check
        if np.dot(arr, np.transpose([-100, -10, -1, 1, 10, 100])) == 0:
            pal = prod

        i += 1
        j -= 1

    range += 1

print pal
