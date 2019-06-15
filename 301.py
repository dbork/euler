# so X is the bitwise-xor of the pile sizes (for arbitrarily many piles) as
# follows (though brice told me it was xor, i doubt i would have quickly
# figured that out):

# if xor = 0, next player's move always makes it nonzero by changing bits
# of even parity to bits of odd parity

# if xor != 0, can change the largest pile to the xor of the others to make it
# zero

# all moves reduce the total, natch, so within (sum of initial pile sizes)
# moves, someone has to reach 0, 0, 0, and, since that has xor 0, that
# someone has to be the xor-zeroer

# so how many n, 2n, 3n configs have xor zero? it'll be true if n and 2n have
# no bits in common, since then xor(n, 2n, 3n = n + 2n) = xor(n, 2n, n, 2n) = 0
# this is also iff, since if n and 2n /do/ have a bit in common, the resulting
# carry bit in 3n has parity not equal to its parity in (n, 2n, n, 2n)
# so it's the number of n less than 2^30 with no two consecutive bits
# which is the number of tilings of a 1 x 31 rectangle w squares and 2x1s
# which is fib(31)
# which is

fibs = [1, 1] + [0 for i in range(30)]
for i in range(2, 32):
    fibs[i] = fibs[i-1] + fibs[i-2]
print fibs[31]
