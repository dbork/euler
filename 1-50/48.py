# mod is good
tendigits = 0
for i in range(1, 1001):
    mod = i
    # i could do iterative doubling but uh
    # i'm lazy
    for j in range(1, i):
        mod =  (mod * i) % (10 ** 10)

    tendigits = (tendigits + mod) % (10 ** 10)

print tendigits
