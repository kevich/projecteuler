#! /usr/bin/env python
# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
# letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive
# were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

# Number to word
#1-9
mainWords = dict()
mainWords[0] = ''
mainWords[1] = 'one'
mainWords[2] = 'two'
mainWords[3] = 'three'
mainWords[4] = 'four'
mainWords[5] = 'five'
mainWords[6] = 'six'
mainWords[7] = 'seven'
mainWords[8] = 'eight'
mainWords[9] = 'nine'
#10-20
mainWords[10] = 'ten'
mainWords[11] = 'eleven'
mainWords[12] = 'twelve'
mainWords[13] = 'thirteen'
mainWords[14] = 'fourteen'
mainWords[15] = 'fifteen'
mainWords[16] = 'sixteen'
mainWords[17] = 'seventeen'
mainWords[18] = 'eighteen'
mainWords[19] = 'nineteen'
mainWords[20] = 'twenty'
#second positions
secondPosition = dict()
secondPosition[2] = 'twenty'
secondPosition[3] = 'thirty'
secondPosition[4] = 'forty'
secondPosition[5] = 'fifty'
secondPosition[6] = 'sixty'
secondPosition[7] = 'seventy'
secondPosition[8] = 'eighty'
secondPosition[9] = 'ninety'

summ = 0

for x in xrange(1,1000):
    mainWord = x%100
    if mainWord in mainWords:
        textMain = mainWords[mainWord]
        summ += len(mainWords[mainWord])
    else:
        textMain = secondPosition[mainWord/10] + "-" + mainWords[mainWord%10]
        summ += len(secondPosition[mainWord/10]) + len(mainWords[mainWord%10])
#hundred - 7, and - 3
    restName = ''
    if x/100 > 0:
        restName = mainWords[x/100] + " hundred"
        summ += len(mainWords[x/100]) + 7
        if x%100 != 0:
            restName += " and"
            summ += 3
    print x, '=', restName, textMain
#one thousand
summ += 3 + 8

print(summ)
#./Problem0017.py  0,02s user 0,01s system 80% cpu 0,043 total
