#! /usr/bin/env python
#Double-base palindromes
#Problem 36
#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic
#in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include
#leading zeros.)

import math

def isPalindrom(string):
    return string == string[::-1]

searchList = list()

x = 1
#1 is polindrom
summa = 1
while x < 1000000:
    #for base 10 number it should be odd so that it will be 1 at the end
    #of binary number
    x += 2
    if (isPalindrom(str(x)) and isPalindrom(str(bin(x)).replace('0b', ''))):
        summa += x
        searchList.append([x, str(bin(x)).replace('0b', '')])

print searchList
print 'Result: ' + str(summa)
#./Problem0036.py  0,26s user 0,01s system 98% cpu 0,529 total
