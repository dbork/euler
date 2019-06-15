import math

from primes import getPrimes 

def count_tilings_lazy(size, tiles, laziness=None):
    #count = 1
    remainders = set({size})
    min_idx = 0
    while min_idx < len(tiles) and tiles[min_idx] < size:
        new_remainders = set({})
        for r in remainders:
            for i in range(1, int(r / tiles[min_idx]) + 1):
                new_remainders.add(r - i * tiles[min_idx])
            #count += len(rem_list)
            if len(remainders) + len(new_remainders) > laziness:
                #print ok i'm bored lol
                return float('inf')
        remainders.update(new_remainders)
        #print count
        #print remainders
        #print len(remainders)
        if len(remainders) > laziness:
            #print 'ok i\'m bored lol'
            return float('inf')
        min_idx += 1
    return len(remainders)

def solve_given_n(n):
    # it's 2^i * something by construction, where the something is composed of
    # 2s, 3/2s, 5/2s, etc. we also know these things can't go higher than
    # the k-th prime, which the prime number theorem says will be less than
    # about ln(n), so just to be safe we can do
    primes = filter(lambda x: x > 0, getPrimes(int(math.log(n, 2) * n)))
    #print primes
    tiles = [math.log(1.5, 2), 1] + map(lambda x: math.log(float(x) / 2, 2), primes[2:])
    #print tiles
    print len(tiles)

    # this is v generous but should be fine
    upper_bound = tiles[0] * n
    # now we binary search for n tilings lol
    guess = 0
    mod_guess = 0
    powers = range(-50, int(math.log(upper_bound, 2)) + 1)
    powers.reverse()
    for power in powers:
        print 'trying power ' + str(power)
        print 'with guess ' + str(guess)
        tilings = count_tilings_lazy(guess + 2 ** power, tiles, n * 50)
        print tilings
        if tilings < n:
            guess += 2 ** power

    print guess
    print (2 ** guess * 2 ** n) #% 123454321

# doesn't work, insufficient precision
solve_given_n(1000)
