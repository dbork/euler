# i don't really understand the theory here at all, but this should be
# easy enough just to calculate...

# the hundredth convergent in particular is
# [2; 1 2 1 1 4 1 1 6 1 ... 1 66 1]
# so just calculate them in reverse order, fine
limit = 100
k = (limit - 1) / 3

num = 0
denom = 1

while k > 0:
	# observe 1/(1 + n/d) = d / (n + d)
	denom += num
	num = denom - num
	# and 1/(2k + n/d) = d / (n + 2kd)
	denom = denom * 2 * k + num
	num = (denom - num) / (2 * k)
	# and now the first one again	
	denom += num
	num = denom - num

	k -= 1

# now we need to add the 2
num += 2 * denom

#print num
#print denom
print sum(map(int, list(str(num))))
