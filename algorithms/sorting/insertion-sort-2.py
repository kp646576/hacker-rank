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

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
