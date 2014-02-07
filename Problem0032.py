#! /usr/bin/env python

# Pandigital products
# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to
# n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, 
# multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written 
# as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it 
# once in your sum.

# 103*98 = 10094 (max number)
# lesser sums will cause not needed 5 digit number


result = list()

def filterUniq(arr):
    return list(set(arr) - set(['0']))
#                  123456789
for a in xrange(1,1000000000):
    b = 1
    while (len(str(a) + str(b) + str(a*b)) < 9):
        b += 1
    if (b == 1):
        break
    b -= 1
    while (len(str(a) + str(b) + str(a*b)) < 10):
        b += 1
        if (len(set(str(a)) & set(str(b))) > 0):
            continue
        product = a * b
        if (len(filterUniq(str(a) + str(b) + str(product))) == 9
            and len(str(a) + str(b) + str(a*b)) == 9):
            result.append(product);
            print a, "*", b, "=", product, "    ", filterUniq(str(a) + str(b) + str(product))
    
print result,filterUniq(result),sum(set(filterUniq(result)))
# ./Problem0032.py  0,37s user 0,01s system 99% cpu 0,380 total