#! /usr/bin/env python
# Factorial digit sum
# Problem 20
# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from math import factorial

print sum(map(int, list(str(factorial(100)))))
#./Problem0020.py  0,01s user 0,01s system 93% cpu 0,025 total
