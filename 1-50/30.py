# stolen from 34.py, but now we want fifth powers, which means our upper
# bound is 531441 = 9^6
print -1 + sum([x for x in range(531441) if list(str(x)) \
        == list(str(sum(map(lambda y: int(y) ** 5, list(str(x))))))]) 
