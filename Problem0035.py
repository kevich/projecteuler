#! /usr/bin/env python
# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all
# rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17,
# 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import math

def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n

def mutations(val):
    mut = []
    for i in range(0, len(str(val))):
        mut.append(str(val)[i:] + str(val)[:i])
    return mut

def isCircularPrime(primes, n):
    isCircularPrime = False
    for num in mutations(n):
        if int(num) in primes:
            continue
        else:
            return False
    return True

x = 1

searchList = list()

while x < 1000000:
    x += 1
    if (len(set(str(x))-set(['1','3','7','9'])) == 0 or len(str(x)) == 1) and isPrime(x):
        searchList.append(x)

count = 0

for num in searchList:
    if isCircularPrime(searchList, num):
        print num
        count += 1

print 'Total count: ' + str(count)

#A circular prime with at least two digits can only consist of
#combinations of the digits 1, 3, 7 or 9, because having 0, 2, 4, 6 or 8
#as the last digit makes the number divisible by 2, and having 0 or 5
#as the last digit makes it divisible by 5
#./Problem0035.py  1,57s user 0,01s system 99% cpu 1,590 total
