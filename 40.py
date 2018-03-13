# i'm lazy
c = ''.join([str(i) for i in range(1000001)])
print int(c[1]) * int(c[10]) * int(c[100]) * int(c[1000]) \
        * int(c[10000]) * int(c[100000]) * int(c[1000000])
