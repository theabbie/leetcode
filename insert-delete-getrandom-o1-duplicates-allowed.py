import bisect
import random

class RandomizedCollection:

    def __init__(self):
        self.items = []
        
    def exists(self, val):
        i = bisect.bisect_left(self.items, val)
        return i < len(self.items) and self.items[i] == val

    def insert(self, val: int) -> bool:
        if not self.exists(val):
            bisect.insort(self.items, val)
            return True
        bisect.insort(self.items, val)
        return False

    def remove(self, val: int) -> bool:
        if self.exists(val):
            del self.items[bisect.bisect_left(self.items, val)]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()