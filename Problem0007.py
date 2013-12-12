#! /usr/bin/env python
# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n

def primeNumber(position):
    number = 0
    n = 1
    count = 3
    while count <= position:
        for x in [6*n-1, 6*n+1]:
            if isPrime(x):
                number = x
                count += 1
        n += 1

    return number

print(primeNumber(6))
print(primeNumber(10001))
#./Problem7.py  0,21s user 0,01s system 83% cpu 0,260 total
