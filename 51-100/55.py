# dp, dictionaries, whatever
def isPalindrome(n):
    l = list(str(n))
    return l[:len(l) / 2 ] == list(reversed(l[(len(l) + 1)/ 2:]))

limit = 10000
notLychrel = [0 for i in range(limit)]
for i in range(limit):
    stack = [i]
    cand = i
    cand = cand + int(''.join(reversed(list(str(cand)))))
    #print cand
    while len(stack) <= 51:
        if isPalindrome(cand) or (cand < limit and notLychrel[cand] == 1):
            for j in filter(lambda x: x < limit, stack):
                notLychrel[j] = 1
            break

        stack.append(cand)
        cand = cand + int(''.join(reversed(list(str(cand)))))
        #print cand
           
print [i for i in range(limit) if notLychrel[i] == 0]
print len(filter(lambda x: x == 0, notLychrel))

