# it's not the simplest imaginable graph thing. so let's think of something
# else that isn't that thing. i say from a position of vague pre-caffeine
# delirium
logins = []
f = open("p079_keylog.txt")
for line in f:
    logins.append(line.rstrip())
f.close()

#print logins

# so i don't really have a plan...i guess i'm just going to try stuff
#print sorted(logins)
logins.sort()
print logins

# oh, whenever 0 appears, it's always last. that's suggestive. let's
# truncate all the 0s and iterate this
#print map(lambda x: str(x).rstrip('0'), sorted(logins))
logins = map(lambda x: str(x).rstrip('0'), sorted(logins))
print logins

# now 9 works
logins = map(lambda x: str(x).rstrip('9'), sorted(logins))
print logins

# now 8 works
logins = map(lambda x: str(x).rstrip('8'), sorted(logins))
print logins

# now 2 works
logins = map(lambda x: str(x).rstrip('2'), sorted(logins))
print logins

# now 6 works
logins = map(lambda x: str(x).rstrip('6'), sorted(logins))
print logins

# then 731. inspection is great. so generalizing this might be awful
# but luckily we don't need to lmao
print 73162890
