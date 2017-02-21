def s1():
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

# Working solution
def s2():
    n, m = map(int, raw_input().strip().split(' '))
    array = [0] * (n + 1) 

    for i in range(m):
        a, b, k = map(int, raw_input().strip().split(' '))
        # Add k to indecies a-1 and b-1
        array[a-1] += k
        array[b] -= k

    # Find maximum value of array
    curMax = 0
    arrMax = 0
    for j in range(n):
        curMax += array[j]
        if curMax > arrMax:
            arrMax = curMax
    print arrMax

'''
---
 ----
  -
----------  
'''
