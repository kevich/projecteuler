#! /usr/bin/env python
# Names scores
# Problem 22
# Using data/problem22.txt file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?


names = open('./data/problem22.txt')
names = sorted(reduce(lambda res,x: res+str(x), list(names), '').replace('"','').split(','))

pos = 1
summ = 0

for name in names:
    summ += (reduce(lambda res,x: res+ord(x)-64, list(name), 0))*pos
    pos += 1

print summ
#./Problem0022.py  0,03s user 0,01s system 95% cpu 0,043 total
