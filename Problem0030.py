#! /usr/bin/env python
# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

res = 0

for x in xrange(2,(9**5)*5):
    summ = 0
    for n in list(str(x)):
        if summ <= x:
            summ += int(n)**5
        else:
            break
    if summ == x:
        print x
        res += x

print 'total', res
#./Problem0030.py  1,88s user 0,01s system 99% cpu 1,890 total
