# so it's 1 plus, for each odd i, 4i^2 - 6(i-1)
# eg 9 + 7 + 5 + 3 = 4(9) - 6(2)
# sum of the even terms from 1 to 1001 of -6i is
# -6(1002)(500/2)
#
# sum of the odd terms from 3 to 1001 of 4i^2 can
# found with the ansatz s(x) = ax^3 + bx^2 + cx + d
# and then s(x+2) = s(x) + 4(x+2)^2
# a(x^3 + 6x^2 + 12x + 8) + b(x^2 + 4x + 4) + c(x+2) + d = ax^3 + bx^2 + cx + d + 4(x^2 + 4x + 4)
#
# const:    8a + 4b + 2c = 16
# x term:   12a + 4b = 16
# x^2 term: 6a = 4
# which gives a = 2/3, b = 2, c = 4/3
# then s(3) = 36 = 2/3(27) + 2(9) + 4/3(3) + d gives d = -4
# (not unreasonably, since we're excluding the 1 term)

# anyway, don't try this on even numbers lol
def sq(x):
    # ints are the worst
    return 1 + (-6 * (x+1) * (x-1)/4) + ((float(2)/3) * x**3 + 2 * x**2 + (float(4)/3) * x - 4)

#print -6 * 6 * 1
#print int(float(2)/3 * 125 + 2 * 25 + float(4)/3 * 5 - 4)
print sq(1001)
