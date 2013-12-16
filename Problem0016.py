#! /usr/bin/env python
# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

print(reduce(lambda res,x: res+x, map(int,list(str(pow(2,1000))))))
#./Problem0016.py  0,01s user 0,01s system 94% cpu 0,026 total
