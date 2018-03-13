# i'm going to do this uninterestingly, sorry
# starting at 1901 to avoid having to deal with leap year weirdness
year = 1901
day = 2 # mod 7
month = 0
months = [31%7,28%7,31%7,30%7,31%7,30%7,31%7,31%7,30%7,31%7,30%7,31%7]
leap = 1 # mod 4
suns = 0

while year < 2001:
    for month in months:
        day = (day + month) % 7
        if month == 0 and not leap:
            day = (day + 1) % 7
        if day == 0:
            suns = suns + 1
    
    leap = (leap + 1) % 4
    year = year + 1

print suns
