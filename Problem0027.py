#! /usr/bin/env python
# Quadratic primes
# Problem 27
# Euler discovered the remarkable quadratic formula:

# n*n + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values
# n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
# by 41, and certainly when n = 41, 41*41 + 41 + 41 is clearly divisible by 41.

# The incredible formula  n*n - 79n + 1601 was discovered, which produces 80 primes
# for the consecutive values n = 0 to 79. The product of the coefficients, -79 and
# 1601, is -126479.

# Considering quadratics of the form:

# n*n + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4 Find
# the product of the coefficients, a and b, for the quadratic expression that
# produces the maximum number of primes for consecutive values of n, starting with
# n = 0.

def formula(n, a, b):
    return n**2+a*n+b

def isPrime(n):
    if n <= 0:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return n

maxNum = 0
foundA = 0
foundB = 0

for a in xrange(-1000,+1000):
    for b in xrange(-1000,+1000):
        n = 0
        while isPrime(formula(n, a, b)):
            n+=1
        if n > maxNum:
            maxNum = n
            foundA = a
            foundB = b

print maxNum, foundA, foundB, foundA*foundB
#./Problem0027.py  5,41s user 0,01s system 99% cpu 5,420 total
