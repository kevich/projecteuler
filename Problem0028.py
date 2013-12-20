#! /usr/bin/env python
# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def spiral(dimention):
    array = [[0 for x in xrange(dimention)] for x in xrange(dimention)] 
    center = dimention/2
    x = y = center
    n = 1
    step = 0
    array[x][y] = n
    while n < dimention**2:
        for count in xrange(1,step/2+1):
            if step%2 == 0:
                y = (y+1) if (step%4<2) else (y-1)
            else:
                x = (x+1) if (step%4<2) else (x-1)
            if n >= dimention**2:
                return array
            n += 1
            array[x][y] = n
        step += 1
    return array

def diagonalsSum(matrix):
    summ = 0
    dimention = len(matrix)
    for x in xrange(0,dimention):
        summ += matrix[x][x] + matrix[x][dimention-1-x]
    return summ - matrix[dimention/2][dimention/2]

print diagonalsSum(spiral(1001))
#./Problem0028.py  0,61s user 0,03s system 99% cpu 0,637 total
