# ok let's speculate

# first off if p is prime, s(p) = p straight-up, so it's at least the sum
# of all the primes.

# then if all of x's prime factors are distinct, s(x) is the largest prime
# factor

# but for 12 = 3 * 2 ** 2, it's 4, fine.

# but then for 8 * 5 = 40, it's 5, whoo. so it's not the largest
# one either way...

# ok, is there a way to ask for any i, how many new ones does it introduce?
# if i is prime the answer is exactly...not one, but whichever ones were
# already divisible and are still less than 10 * 8 when multipled by i...ok

# so step one is sum the primes, fine.
# then step 2: for all factors less than 10 ** 4...
# how many /distinct new prime factorizations less than 10 ** 8/ does i
# create? if i was prime, you can sum all the previously covered ones
# less than 10 ** 8 / i

# no, here's how you do it with a modded sieve. first sum all the primes and
# set them to 0 in a new sieve list. then you go through /all/ the numbers
# less than 10 ** 4 and sieve them up, adding the number to the total
# every time you set a new counter to 0, and at the end you're guaranteed
# to get them all. though it's not quite that simple...6 doesn't fix only
# multiples of 6, it fixes only multiples of 3 ** 2 or 2 ** 4, since its the
# second 3 and the fourth 2...annoying but probably fine to do by just
# maintaining a 1000-length list of how many factors you've encountered and
# trial-divisioning to prime factorize

# buuut i also just don't want to do this rn lol
