n, m = map(int, raw_input().strip().split(' '))
array = [0] * n

for i in range(m):
    a, b, k = map(int, raw_input().strip().split(' '))
    
    # Add k to indecies a-1 to b-1
    for j in range(a-1, b):
        array[j] += 1

# Find maximum value of array
print max(array)
#maxIdx = array.index(max(array))



'''
---
 ----
  -
----------  
'''
