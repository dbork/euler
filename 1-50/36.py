# so i think the fastest (from a me-coding-it perspective) way to do this is
# just to write a palindrome function
def pal(l):
    revEnd = l[(len(l) + 1) / 2:]
    revEnd.reverse()
    return l[:len(l) / 2] == revEnd

numList = [list(str(x)) for x in range(1000001)]
base10pals = filter(pal, numList)
base2 = map(lambda x: list(str(bin(int(''.join(x)))))[2:], base10pals)
base2pals = filter(pal, base2)
print sum(map(lambda x: int(''.join(x), 2), base2pals))
