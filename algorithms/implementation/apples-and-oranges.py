#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

house = [0, 0]
for i in apple:
    if a + i >= s and a + i <= t:
        house[0] += 1
for j in orange:
    if b + j >= s and b + j <= t:
        house[1] += 1

print house[0]
print house[1]
