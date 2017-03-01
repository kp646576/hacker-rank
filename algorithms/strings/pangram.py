import re
import string
import sys

def pangram(letters, s):
    for l in letters:
        if not re.search(r'{0}|{1}'.format(l, l.upper()), s):
            print 'not pangram'
            return
    print 'pangram'

s = raw_input().strip()
letters = list(string.ascii_lowercase)
pangram(letters, s)


'''
s = input().strip()
alphabet ='abcdefghijklmnopqrstuvwxyz'
if all(l in s.lower() for l in alphabet):
    print('pangram')
else:
    print('not pangram')
'''
