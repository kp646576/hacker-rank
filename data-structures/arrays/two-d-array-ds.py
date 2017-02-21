#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

sums = []
# 0 - 3
for i in range(4):
    for j in range(4):
        top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        mid = arr[i + 1][j + 1]
        bot = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        sums.append(top + mid + bot)

print max(sums)

# arr[0][0-2] + arr[1][1] + arr[2][0-2] # arr[1][0-2] + arr[2][1] + arr[3][0-2] ...
# arr[0][1-3] + arr[1][2] + arr[2][1-3] # arr[1][1-2] + arr[2][2] + arr[3][1-3] ...
# ...
