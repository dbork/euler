# um, it can't be constant with respect to n, since it's 9 for n = 1
# and 6 for n = 2. so what's the limit? has to be less than 10,
# since 10^n has n + 1 digits. meanwhile 9^9 = 10^10 * (9/10)^n,
# which will quickly fall below 10, giving a limit of 0. i don't get it...

# OH IT'S A SUM OVER ALL N LMAO WHAT AM I DOING

# OK

total = 3

# 4 works twice
total += 2

# 5 works 3 times
total += 3

# 6 works 4 times
total += 4

# 7 works 6 times
total += 6

# 8 works 10 times
total += 10

# 9 works 21 times
total += 21

print total
