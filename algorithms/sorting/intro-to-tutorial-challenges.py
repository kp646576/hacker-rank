v = int(raw_input())
n = int(raw_input())
arr = map(int, raw_input().strip().split(' '))

for i in range(n):
    if (arr[i] == v):
        print i

#print arr.index(v)
