#! /usr/bin/env python
# Maximum path sum I
# Problem 18
# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

triangle = [
map(int,'75'.split(' ')),
map(int,'95 64'.split(' ')),
map(int,'17 47 82'.split(' ')),
map(int,'18 35 87 10'.split(' ')),
map(int,'20 04 82 47 65'.split(' ')),
map(int,'19 01 23 75 03 34'.split(' ')),
map(int,'88 02 77 73 07 63 67'.split(' ')),
map(int,'99 65 04 28 06 16 70 92'.split(' ')),
map(int,'41 41 26 56 83 40 80 70 33'.split(' ')),
map(int,'41 48 72 33 47 32 37 16 94 29'.split(' ')),
map(int,'53 71 44 65 25 43 91 52 97 51 14'.split(' ')),
map(int,'70 11 33 28 77 73 17 78 39 68 17 57'.split(' ')),
map(int,'91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' ')),
map(int,'63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' ')),
map(int,'04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' '))
]

def maxSum(row, item):
    data = triangle[row][item]
    nextRow = row + 1
    if nextRow == len(triangle):
        return data
    else:
        return max([data + maxSum(nextRow,item), data + maxSum(nextRow,item + 1)])
    

print maxSum(0,0)
