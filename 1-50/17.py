# one   3 six   3   ten    3 sixty   5   hundred  7
# two   3 seven 5   twenty 6 seventy 7   thousand 8
# three 5 eight 5   thirty 6 eighty  6   
# four  4 nine  4   forty  5 ninety  6   and 3
# five  4           fifty  5
#
# eleven 6 twelve 6 thirteen 8 fifteen 7 eighteen 8

# how many ones? 9 per hundred = 90, plus 100 in 100,
# plus one in a thousand.

# so each digit in 1-9 gets 190, and 1 gets an extra.
digits = 3 * 191 + (3+5+4+4+3+5+5+4) * 190

# for 20-90, there is just ten per hundred
tensplace = 100 * (6+6+5+5+5+7+6+6)

# 10-19 appear once per hundred
teens = 10 * (3+6+6+8+8+7+7+9+8+8)

# hundred appears 900 times
hundreds = 7 * 900

# thousand appears once
thousand = 8

# and appears 891 times, showing up only after hundred
# but not for exact multiples of 100
ands = 3 * 891

# so the total is...
print digits + tensplace + teens + hundreds + thousand + ands
