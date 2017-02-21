def ransom_note(magazine, ransom):
    for word in ransom:
        if word not in magazine:
            return False
        magazine.remove(word)
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
