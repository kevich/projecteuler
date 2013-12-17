#! /usr/bin/env python
# Lexicographic permutations
# Problem 24 
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all of the permutations are listed numerically or
# alphabetically, we call it lexicographic order. The lexicographic
# permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

# lets say we have 0 first then all the permutations with leading 0 will be:
# 9! = 362880
# same with leading 1
# totally will have 9! + 9! = 725760
# so the millionth lexicographic permutation will start with number 2
# let's find exact, supposing 2013456789 is 725761
# So lets do this automatically in script:

import math

i = 9
numbers = list('0123456789')
total = 999999
num = ''

while total > 0:
    factorial = math.factorial(i)
    nextNum = numbers[total/factorial]
    num += nextNum
    numbers.remove(nextNum)
    total = total%factorial
    i = i - 1

print num+''.join(numbers)
#./Problem0024.py  0,01s user 0,01s system 93% cpu 0,026 total
    