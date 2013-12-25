#! /usr/bin/env python
# Coin sums
# Problem 31
# In England the currency is made up of pound, pound, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, pound1 (100p) and pound2 (200p).
# It is possible to make pound2 in the following way:

# 1xpound1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can pound2 be made using any number of coins?

#http://en.wikipedia.org/wiki/Change-making_problem

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0]*target
 
for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print ways[target]
#./Problem0031.py  0,01s user 0,01s system 17% cpu 0,116 total
