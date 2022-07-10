class SmallestInfiniteSet:

    def __init__(self):
        self.minval = 1
        self.removed = set()

    def popSmallest(self) -> int:
        while self.minval in self.removed:
            self.minval += 1
        self.removed.add(self.minval)
        return self.minval

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        self.minval = min(self.minval, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)