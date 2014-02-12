#! /usr/bin/env python

# Digit canceling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

def gcd(a, b):
#Calculate the Greatest Common Divisor of a and b.
    while b:
        a, b = b, a%b
    return a

numenator = 1
denominator = 1

for x in xrange(10,99):
    for y in xrange(10,99):
        common = set(str(x))&set(str(y))-set(['0'])
        if len(common) > 0:
            xMod = ''.join(set(str(x))-common)
            if xMod == '':
                xMod = ''.join(common)
            yMod = ''.join(set(str(y))-common)
            if yMod == '':
                yMod = ''.join(common)
            if int(yMod) > 0 and x/y < 1 and float(x)/float(y) == float(xMod)/float(yMod):
                print x,'/',y,'=',xMod,'/',yMod,'=',float(x)/float(y)
                numenator *= int(xMod)
                denominator *= int(yMod)
                
print denominator/gcd(numenator,denominator)
#./Problem0033.py  0,05s user 0,01s system 97% cpu 0,064 total
