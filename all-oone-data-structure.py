from collections import defaultdict
import heapq

class AllOne:
    def __init__(self):
        self.ctr = defaultdict(int)
        self.deleted = defaultdict(int)
        self.minheap = []
        self.maxheap = []

    def inc(self, key: str) -> None:
        self.deleted[(self.ctr[key], key)] += 1
        self.deleted[(-self.ctr[key], key)] += 1
        self.ctr[key] += 1
        heapq.heappush(self.minheap, (self.ctr[key], key))
        heapq.heappush(self.maxheap, (-self.ctr[key], key))

    def dec(self, key: str) -> None:
        if self.ctr[key] > 0:
            self.deleted[(self.ctr[key], key)] += 1
            self.deleted[(-self.ctr[key], key)] += 1
            self.ctr[key] -= 1
            heapq.heappush(self.minheap, (self.ctr[key], key))
            heapq.heappush(self.maxheap, (-self.ctr[key], key))

    def getMaxKey(self) -> str:
        while len(self.maxheap) > 0 and self.deleted[self.maxheap[0]] > 0:
            self.deleted[self.maxheap[0]] -= 1
            heapq.heappop(self.maxheap)
        if len(self.maxheap) > 0:
            return self.maxheap[0][1]
        return ""

    def getMinKey(self) -> str:
        while len(self.minheap) > 0 and self.deleted[self.minheap[0]] > 0:
            self.deleted[self.minheap[0]] -= 1
            heapq.heappop(self.minheap)
        if len(self.minheap) > 0:
            return self.minheap[0][1]
        return ""