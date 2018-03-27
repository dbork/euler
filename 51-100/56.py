# lol python
print max(map(lambda x: sum(map(int, list(str(x)))), \
          [a ** b for a in range(100) for b in range(100)]))
