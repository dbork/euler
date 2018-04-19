# so it sure looks like, at each iteration, we set the new denominator
# equal to num + denom and the new numerator equal to num + 2 * denom

# observe that if the fraction were sqrt(2)/1, this gives
# sqrt(2) + 2 / sqrt(2) + 1 * sqrt(2) - 1 / sqrt(2) - 1 = sqrt(2) / 1,
# so this procedure does definitely converge to what we want...

(n, d) = (3, 2)
count = 0
for i in range(1000):
    (n, d) = (n + 2 * d, n + d)
    if len(str(n)) > len(str(d)):
        count += 1
print count

# this works, but, troublingly, i don't reeeally understand why all the way.
# eg why the expansion follows the pattern i observed... the math doesn't
# immediately work out as nicely as i want it to... :(
