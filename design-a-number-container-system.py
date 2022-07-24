import bisect
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.vals = {}
        self.pos = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.vals:
            i = bisect.bisect_left(self.pos[self.vals[index]], index)
            if i < len(self.pos[self.vals[index]]):
                self.pos[self.vals[index]].pop(i)
        bisect.insort(self.pos[number], index)
        self.vals[index] = number

    def find(self, number: int) -> int:
        if number in self.pos and len(self.pos[number]) > 0:
            return self.pos[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)