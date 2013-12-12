#! /usr/bin/env python
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrom(number):
    tempNumber = number
    revertedNumber = 0
    while tempNumber > 0:
        revertedNumber = revertedNumber * 10 + tempNumber%10
        tempNumber = tempNumber / 10
    if revertedNumber == number:
        return True
    else:
        return False

maximum = 0

for x in xrange(999, 100, -1):
    for y in xrange(999, 100, -1):
        if (isPalindrom(x*y)):
            if x*y > maximum:
                maximum = x*y

print(maximum)
#./Problem4.py  1,54s user 0,01s system 99% cpu 1,550 total
