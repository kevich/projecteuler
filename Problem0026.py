#! /usr/bin/env python
# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:

# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

# Found that bigger number - bigger recurring, and it's length of 
# recurring not bigger than number
# So for faster solution lets check last 50 numbers
# mantis will be 1000*2 to expect if we have 1000 length recurring - 
# we will find it

from decimal import *

def uniq(arr):
    return list(set(arr))

getcontext().prec = 2000

maximum = 0
number = 0
realWorld = ''

for x in xrange(950,1000):
    stringRepresentation = str(Decimal(1)/x).replace('0.', '')
    reqCycle = []
    realReq = ''
    print '##',x
    for i,y in enumerate(stringRepresentation):
        reqCycle.append(y)
        if ''.join(uniq(stringRepresentation[i:])) == '0':
            break
        if len(reqCycle) > 0:
            gotSame = False
            for z in xrange(0,len(reqCycle)):
                if (stringRepresentation[i:i+len(reqCycle[z:])-1] == ''.join(reqCycle[z:-1])
                and ''.join(set(stringRepresentation[i:].replace(''.join(reqCycle[z:-1]), ''))-set(reqCycle[z:-1])) == ''):
                    gotSame = True
                    realReq = ''.join(reqCycle[z:-1])
                    break
            if gotSame:
                break
    word = ''.join(stringRepresentation[0:i])
    if len(realReq) > maximum:
        maximum = len(realReq)
        print x, maximum
        number = x
        realWorld = stringRepresentation

print number, maximum, realWorld
#./Problem0026.py  121,72s user 0,09s system 99% cpu 2:01,96 total
