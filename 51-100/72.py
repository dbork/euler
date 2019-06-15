# use totients
import sys
sys.path.append("..")
import totients

limit = 1000000
# 1/1 doesn't count
print sum(totients.getTotients(limit)[2:])
