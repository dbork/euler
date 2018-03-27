# this seems amenable to itertools
import itertools as it

f = open("p059_cipher.txt")
text = f.readline().rstrip().split(',')
f.close()

# but can i remember the itertools syntax without having to reread the page,
# as is Mandated By Law if i fail??

# first, let's try partitioning the values based on key
first = [text[3 * i] for i in range((len(text) - 1) / 3)]
second = [text[3 * i + 1] for i in range((len(text) - 1) / 3)]
third = [text[3 * i + 2] for i in range((len(text) - 1) / 3)]

firstCounts = {i: first.count(i) for i in first}
secondCounts = {i: second.count(i) for i in second}
thirdCounts = {i: third.count(i) for i in third}

print first
print second
print third
print "firstCounts"
print firstCounts
print sorted(firstCounts.keys(), key=lambda x: firstCounts[x])
print "secondCounts"
print secondCounts
print sorted(secondCounts.keys(), key=lambda x: secondCounts[x])
print "thirdCounts"
print thirdCounts
print sorted(thirdCounts.keys(), key=lambda x: thirdCounts[x])

# and, what do you know, all three of these have a most-occurred-character
# that is very far from the others in their partition and very close to the
# other two most-frequent-characters. betcha that's spacebar

# ok, respectively these putative spaces are 71, 79, and 68
key1 = ord(' ') ^ 71
key2 = ord(' ') ^ 79
key3 = ord(' ') ^ 68

# now we will continue the approach with practices consistent with our chosen
# langauge of print statements to verify this by inspection 
print map(lambda x: chr(int(x) ^ key1), first)
print map(lambda x: chr(int(x) ^ key2), second)
print map(lambda x: chr(int(x) ^ key3), third)

# Why Look At That, They're All Letters >:)
keys = [key1, key2, key3]
decoded = ''.join([chr(int(text[i]) ^ keys[i % 3]) for i in range(len(text))])
print decoded
print sum(map(ord, list(decoded)))
