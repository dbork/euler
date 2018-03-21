# this should be fast just with the straightforward approach, and i don't
# see any obvious neat math
f = open("p042_words.txt")
words = f.readline().strip("\"").split("\",\"")
f.close()

charConst = 64

def alphaSum(s):
    return sum(map(lambda x: ord(x) - charConst, list(s)))

# English words are not really longer than ~20 characters, so we only need
# triangle numbers less than 500 (in practice, even this bound is probably
# pretty loose). so we need at most like 35 or so triangle numbers:
triangles = [n * (n + 1) / 2 for n in range(1, 35)]

print sum(map(lambda x: alphaSum(x) in triangles, words))
