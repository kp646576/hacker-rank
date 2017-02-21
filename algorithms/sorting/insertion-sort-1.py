#!/bin/python
def insertionSort(ar):
    size = len(ar) - 1
    v = ar[size]
    notInserted = True
    count = size - 1
    
    while notInserted:
      if ar[count] > v:
          ar[count + 1] = ar[count]
          if count == 0:
              print ' '.join(map(str, ar)) 
              ar[0] = v
      elif ar[count] <= v:
        ar[count + 1] = v
        notInserted = False
      
      count -= 1
      print ' '.join(map(str, ar))  
        
    return ''

# Test Case 2 broken (does not pass)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
