import random

class RandMemory:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self._history = list()
        
    @property
    def get(self):
        newnum = random.randint(self.lowest, self.highest)
        self._history.append(newnum)
        return newnum
    
    def history(self):
        return self._history