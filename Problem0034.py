#! /usr/bin/env python
# Digit factorials
# Problem 34
# 145 is a curious number, as
# 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to 
# the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they
# are not included.

# 9!*7 = 2540160
# 9!*8 = 2903040

factorials = {
    0:1,
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880
}

def factorialSum(number):
    summ = 0
    while (number > 0):
        d = number % 10;
        number /= 10;
        summ += factorials[d];
    return summ

found = list()

for number in xrange(10,2540161):
    fact = factorialSum(number)
    if fact == number:
        found.append(number)

print found, sum(found)
#./Problem0034.py  5,53s user 0,01s system 99% cpu 5,542 total
