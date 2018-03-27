# um, isn't this just, for every denominator n, a fraction is not unique
# if and only if the numerator is a divisor of n? self-reducibility
# should mean we can legit just sum them
limit = 8

# wait, nnnope. it's the set of numbers that are /mutually prime/ to n, duh
# hmm maybe, just maybe, i should do the totient one first. there straight-up
# must be a way to do this more efficiently than brute-force, 10^12 is well
# beyond the reasonableness threshold
