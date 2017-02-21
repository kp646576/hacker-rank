# n = number of integers
# d = number of left rotations
# array = initial state of integer array
n, d = map(int, raw_input().strip().split(' '))
array = map(int, raw_input().strip().split(' '))
leftRotations = d % n


# Simplest Solution
rotated = array[leftRotations: ] + array[: leftRotations]
print ' '.join(map(str, rotated))

# Manually
# Start at index leftRotations - 1
# Push value to end 
# Push value of leftRotations - 2 if leftRotations - 2 > 0 to end
# Repeat previous step until conditional is false


# Algorithm times out
'''
for i in range(leftRotations):
    # 1 less swap than number of elements
    for j in range(n-1):
        # Swapping algorithm
        tmp = array[j]
        array[j] = array[j+1]
        array[j+1] = tmp
        #Only works on numbers
        #[0] = a + b
        #[1] = [0] - [1] = a
        #[0] = [0] - [1] = b

print ' '.join(map(str, array))
'''

'''
      0                 1                 2                 3                 4
1, 2, 3, 4, 5 --> 2, 3, 4, 5, 1 --> 3, 4, 5, 1, 2 --> 4, 5, 1, 2, 3 --> 5, 1, 2, 3, 4

Every 'n' left rotations results in the same initial sequence

d % n = which rotation pattern [0 - (n-1)] --> how many left rotations you need to make
you will need to make at most (n - 1) left rotations for any 'd'

index: 0 - 1, 1 - 2, 2 - 3, ... , (n-2) - (n-1)

O(n-1) * O(n-1) = O(n^2)
'''
