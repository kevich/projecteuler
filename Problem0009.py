#! /usr/bin/env python
# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def findABC():
    for a in xrange(1,1001):
        for b in xrange(a+1,1001):
            if pow(a,2) + pow(b,2) == pow((1000-a-b),2):
                return [a,b,(1000 - a - b)]

print(reduce(lambda res,x: res*x, findABC()))
#./Problem9.py  0,11s user 0,01s system 75% cpu 0,153 total
