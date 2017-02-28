def superReduced(s):
    notReduced = True
    i = 0
    while s and notReduced:
        if i < len(s) - 1 and s[i] == s[i + 1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
        if i == len(s):
            notReduced = False     
    print s if s else 'Empty String'

def alternativeSolution(s):
      # i: to iterate over the string, starting at 1.
      i = 1
      # While the iterator hasn't exceeded the remaining.
      while i < len(string):
          cur, pre = string[i], string[i-1]
          # Compare characters that are together.
          if cur == pre:
              # If they are equal, remove them from the string
              string = string[:i-1] + string[i+1:]
              # After removal, set back the iterator by two,
              # or if it gets negative, put it at the start.
              i = max(i-2, 0)
          # Advance the iterator.
          i += 1
      if string == "":
          print "Empty String"
      else:
          print string
    
s = raw_input()
superReduced(s)
