#! /usr/bin/env python
# Maximum path sum II
# Problem 67
# By starting at the top of the triangle below and moving to
# adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in data/problem67.txt

triangle = open('./data/problem67.txt')

def prepareRow(row):
    return map(int, row.split(' '))

triangle = map(prepareRow, list(triangle))

def maxSum(row, item):
    data = triangle[row][item]
    nextRow = row + 1
    if nextRow == len(triangle):
        return data
    else:
        return max([data + maxSum(nextRow,item), data + maxSum(nextRow,item + 1)])

print maxSum(0,0)
