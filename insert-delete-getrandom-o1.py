import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            i = self.pos[val]
            self.pos[self.vals[-1]] = i
            del self.pos[val]
            self.vals[i], self.vals[-1] = self.vals[-1], self.vals[i]
            self.vals.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.vals[random.randint(0, len(self.vals) - 1)]