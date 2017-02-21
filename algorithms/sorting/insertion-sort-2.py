#!/bin/python
def insertionSort(ar):
    for i in range(1, len(ar)):
      # n-1 comparisons
      for j in range(i + 1):
          if ar[i] < ar[j] or j == i:
              value = ar[i]
              # Move everything to the right
              for k in range(i, j - 1, -1):
                tmp = ar[k]
                ar[k] = ar[k - 1]
              ar[j] = value
              break
      print ' '.join(map(str, ar))
    return ""

def insertionSort2(ar):
    for i in range(1, len(ar)):
        value = ar[i]
        j = i - 1
        while ar[j] >= value and j >= 0:
            ar[j + 1] = ar[j]
            j -= 1
            ar[j + 1] = value
              
        print ' '.join(map(str, ar))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
