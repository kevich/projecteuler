#! /usr/bin/env python
# Non-abundant sums Problem 23 A perfect number is a number for which the sum
# of its proper divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
# that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

def divisorsSum(n):
    summ = 0
    sqroot,t = int(n**0.5),0
    for factor in xrange(1,sqroot+1):
            if n % factor == 0:
                    summ += factor + n/factor
                    #print factor, n/factor
                    t += 2 # both factor and N/factor
    if sqroot*sqroot == n:
        t = t - 1 # if sqroot is a factor then we counted it twice, so subtract 1
        summ -= sqroot
    return summ - n

def isAbundant(n):
    if divisorsSum(n) > n:
        return True
    else:
        return False
    

resArr = list()
allAbundantNumbersTo28123 = list()
for x in xrange(1,28123):
    if isAbundant(x):
        allAbundantNumbersTo28123.append(x)

canBeSumOfAbundant = list()

for x in xrange(0,len(allAbundantNumbersTo28123)):
    for y in xrange(x,len(allAbundantNumbersTo28123)):
        summ = allAbundantNumbersTo28123[x] + allAbundantNumbersTo28123[y]
        if summ <= 28123:
            canBeSumOfAbundant.append(summ)

print sum(set(range(1,28123)) - set(canBeSumOfAbundant))
#./Problem0023.py  8,85s user 0,22s system 99% cpu 9,075 total
