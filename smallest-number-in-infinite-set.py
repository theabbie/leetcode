import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.seen = set()
        self.end = 1

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            val = heapq.heappop(self.heap)
            self.seen.remove(val)
            return val
        self.end += 1
        return self.end - 1

    def addBack(self, num: int) -> None:
        if num < self.end and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)