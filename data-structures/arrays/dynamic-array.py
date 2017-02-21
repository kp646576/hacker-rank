# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Setup
n, q = map(int, raw_input().strip().split(' '))
lastAns = 0
seq = []
for i in range(n):
    seq.append([])

# Computation
for i in range(q):
    query, x, y = map(int, raw_input().strip().split(' '))
    
    # Find idx at seqList[(x ^ lastAns) % n]
    idx = (x ^ lastAns) % n
    
    # q1
    if (query == 1):
        # Append 'y' to sequence seq
        seq[idx].append(y)

    # q2
    else:
        # Find value of y % size of seq in seq and assign to lastAns
        lastAns = seq[idx][y % len(seq[idx])]
        
        # Print the new value of lastAns on a new line
        print lastAns
