from sortedcontainers import SortedList
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.vals = {}
        self.pos = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.vals:
            self.pos[self.vals[index]].remove(index)
        self.pos[number].add(index)
        self.vals[index] = number

    def find(self, number: int) -> int:
        if len(self.pos[number]) > 0:
            return self.pos[number][0]
        return -1