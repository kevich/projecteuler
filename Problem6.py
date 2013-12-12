#! /usr/bin/env python
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

import math

sqrSum = pow(reduce(lambda res,x: res+x, xrange(1,101)),2)
sumSqr = reduce(lambda res,x: res+pow(x, 2), xrange(1,101))

print(str(sqrSum) + "-" + str(sumSqr) + "=" + str(sqrSum-sumSqr))
#./Problem6.py  0,01s user 0,01s system 37% cpu 0,057 total