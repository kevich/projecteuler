#! /usr/bin/env python
# Lattice paths
# Problem 15
# Starting in the top left corner of a 2x2 grid, and only 
# being able to move to the right and down, there are 
# exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

import math

x = 20
y = 20
#lattice path
print(math.factorial(x+y)/(math.factorial(x)*math.factorial(y)))

#./Problem0015.py  0,01s user 0,01s system 93% cpu 0,024 total