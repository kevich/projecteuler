#! /usr/bin/env python
# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b 
# are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
# so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# dirty hack: http://en.wikipedia.org/wiki/Amicable_numbers
#print sum([220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368])

#number of divisors
def divisorsSum(n):
    summ = 0
    sqroot,t = int(n**0.5),0
    for factor in xrange(1,sqroot+1):
            if n % factor == 0:
                    summ += factor + n/factor
                    t += 2 # both factor and N/factor
    if sqroot*sqroot == n: t = t - 1 # if sqroot is a factor then we counted it twice, so subtract 1
    return summ - n

summ = 0
for x in xrange(2,10000):
    y = divisorsSum(x)
    if y > x:
        if divisorsSum(y) == x:
            summ += x + y

print summ
#./Problem0021.py  0,11s user 0,01s system 80% cpu 0,145 total
