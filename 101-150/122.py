# easy enough with BFS, which has exponential time but in the longest
# answer, which shouldn't be more than 15 or so. oh and you only need one
# BFS tree to fill in the whole table if you add stuff whenever it's
# first encountered. but is there a closed-form? i kinda doubt it, since this
# seems so subset-summy. let's try the BFS, then, if it works, you can look
# up if there's some better way? certainly the low max k also suggests that
# there probably isn't, at least order-of-magnitude-asymptotically...
