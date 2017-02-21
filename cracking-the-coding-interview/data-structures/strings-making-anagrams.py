import string

# guaranteed lowercase
def count_letters(array):
    letters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    
    for l in array:
        letters[l] += 1

    return letters


def number_needed(a, b):
    # sort a and b
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    
    # count letters
    counted_a = count_letters(sorted_a)
    counted_b = count_letters(sorted_b)
    
    # take the lower of the two values numbers_needed += |ai - bi|
    count = 0
    for l in list(string.ascii_lowercase):
        count += abs(counted_a[l] - counted_b[l])
    
    return count

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
