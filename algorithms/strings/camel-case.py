#!/bin/python

import sys

def wordCount(s):
    count = 1
    for c in s:
        if c.upper() == c:
            count += 1
    print count

def wordCount2(s):
    regex = r"[A-Z]"
    print(len(re.findall(regex, s)) + 1)

s = raw_input().strip()
wordCount(s)
