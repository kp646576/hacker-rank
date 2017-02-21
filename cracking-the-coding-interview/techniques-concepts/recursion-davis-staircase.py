cache = {}
def steps(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if n not in cache:
        value = steps(n - 1) + steps(n - 2) + steps(n - 3)
        cache[n] = value
    return cache[n]

s = int(raw_input().strip())
for a0 in xrange(s):
    h = int(raw_input().strip())
    print steps(h)
