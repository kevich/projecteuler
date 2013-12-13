#! /usr/bin/env python
# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although 
# it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

def syracuseCount(n):
    count = 1
    while n > 1:
        if n%2 != 0:
            n = 3*n + 1
        else:
            n = n / 2
        count += 1
    return count

maximum = 0
number = 0

for x in xrange(1,1000000):
    count = syracuseCount(x)
    if count > maximum:
        maximum = count
        number = x

print number, maximum
#./Problem0014.py  42,65s user 0,04s system 99% cpu 42,721 total
