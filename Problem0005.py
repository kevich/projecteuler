#! /usr/bin/env python
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def getNumber():
    number = 1
    while True:
        for x in xrange(1,21):
            if number%x != 0:
                number = number + 1
                break
        if x == 20:
            return number

print(getNumber())
#./Problem5.py  182,39s user 0,14s system 99% cpu 3:02,59 total
