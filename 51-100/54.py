# this seems nice and mindless
p1 = 0
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,\
         'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

f = open("p054_poker.txt")
for line in f:
    
    # parse
    handList = line.rstrip().split(' ')
    hand1 = handList[:5]
    hand2 = handList[5:]
    
    cards1 = map(lambda x: x[0], hand1)
    cards2 = map(lambda x: x[0], hand2)
    suits1 = map(lambda x: x[1], hand1)
    suits2 = map(lambda x: x[1], hand2)
    vals1 = sorted(map(lambda x: cards[x], cards1))
    vals2 = sorted(map(lambda x: cards[x], cards2))

    # first, some properties common to multiple hands
    # need a fix for multiple tying best cards
    flush1 = len(set(suits1)) == 1
    flush2 = len(set(suits2)) == 1
    counts1 = map(lambda x: vals1.count(x), vals1)
    counts2 = map(lambda x: vals2.count(x), vals2)
    bestTuple1 = max(counts1)
    bestTuple2 = max(counts2)
    tupleVal1 = max(filter(lambda x: vals1.count(x) == bestTuple1, vals1))
    tupleVal2 = max(filter(lambda x: vals2.count(x) == bestTuple2, vals2))
    straight1 = bestTuple1 == 1 and max(vals1) - min(vals1) == 4
    straight2 = bestTuple2 == 1 and max(vals2) - min(vals2) == 4
    
    # check for hands in decreasing order of goodness

    # straight flush
    sf1 = straight1 and flush1
    sf2 = straight2 and flush2
    if sf1:
        if not sf2:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif sf2:
        continue

    # four of a kind
    if bestTuple1 == 4:
        if bestTuple2 < 4:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif bestTuple2 == 4:
        continue

    # full house
    fs1 = set(counts1) == set([2, 3])
    fs2 = set(counts2) == set([2, 3])
    if fs1:
        if not fs2: 
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif fs2:
        continue

    # flush
    if flush1:
        if not flush2:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif flush2:
        continue

    # straight
    if straight1:
        if not straight2:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif straight2:
        continue

    # 3 of a kind
    if bestTuple1 == 3:
        if bestTuple2 < 3:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif bestTuple2 == 3:
        continue

    # 2 pairs
    tp1 = bestTuple1 == 2 and counts1.count(2) == 4 
    tp2 = bestTuple2 == 2 and counts2.count(2) == 4 
    if tp1:
        if not tp2: 
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif tp2:
        continue

    # 1 pair
    if bestTuple1 == 2:
        if bestTuple2 < 2:
            p1 += 1
            continue
        elif tupleVal1 > tupleVal2:
            p1 += 1
            continue
    elif bestTuple2 == 2:
        continue

    # high card
    if tupleVal1 > tupleVal2:
        p1 += 1
        continue
    else:
        continue

f.close()

print p1
