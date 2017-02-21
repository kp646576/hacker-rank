class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    # For printing purposes (unambiguous)
    def __repr__(self):
        return self.name + ' ' + str(self.score)
    
    def comparator(a, b):
        # Decreasing order
        if a.score > b.score:
          return -1
        elif a.score < b.score:
          return 1
        elif a.score == b.score:
            if a.name > b.name:
              return 1
            elif a.name < b.name:
              return -1
            else:
              return 0
        return 0
