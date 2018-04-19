# bouncy
# closed-form for increasing numbers less than n?
# if n has at least 9 digits, maxDistinctDigits is 9, otherwise
# it is the number of digits in n

import math

def increasing(n):
    maxDistinctDigits = min(9, int(math.log(n, 10) + 1))
    

# decreasing numbers are NOT the same because of 0
