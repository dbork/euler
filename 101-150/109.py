# so what this is really asking is what's 42336 minus the number of ways to
# checkout with a score more than 100 lol

# assume wlog score(1) > score(2)
doubles = [2 * i for i in range(1, 21)] + [50]
doubles.reverse()
singles = [i for i in range(1, 21)]
all_scores = sorted(singles + map(lambda x: 2 * x, singles)
                    + map(lambda x: 3 * x, singles) + [0, 25, 50], reverse=True)

print doubles
print all_scores

def checkouts(min_score):
    count = 0
    for last in doubles:
        for first_idx in range(len(all_scores)):
            for second_idx in range(first_idx, len(all_scores):
                sum_scores = last + all_scores[first_idx] + all_scores[second_idx]
