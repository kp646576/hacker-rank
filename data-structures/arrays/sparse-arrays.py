n = int(raw_input())
d = {}
for i in range(n):
    entry = raw_input()
    if entry not in d:
        d[entry] = 1
    else:
        d[entry] += 1

q = int(raw_input())
for j in range(q):
    query = raw_input()
    if query not in d:
        print 0
    else:
        print d[query]
