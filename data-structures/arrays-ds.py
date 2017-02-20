#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# Print all N integers in A in reverse order as a single line of space-separated integers.

def s1(arr):
    print ' '.join(map(str, arr[::-1]))

def s2(n, arr):
    for i in reversed(range(n)):
        print arr[i],

#s1(arr)
s2(n, arr)
