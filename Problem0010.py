#! /usr/bin/env python
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n

def primesSum(biggest):
    sumIs = 2 + 3
    n = 1
    number = 0
    while True:
        for x in [6*n-1, 6*n+1]:
            if isPrime(x):
                if x > biggest:
                    return sumIs
                sumIs += x
                number = x
        n += 1

    return sumIs

print(primesSum(10))
print(primesSum(2000000))
#./Problem0010.py  10,99s user 0,01s system 99% cpu 11,005 total
