import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = []
        self.r = []
        for el in nums:
            self.add(el)

    def add(self, val: int) -> int:
        if not self.l or val > -self.l[0]:
            heapq.heappush(self.r, val)
        else:
            heapq.heappush(self.l, -val)
        while len(self.r) < len(self.l):
            heapq.heappush(self.r, -heapq.heappop(self.l))
        while len(self.r) > self.k:
            heapq.heappush(self.l, -heapq.heappop(self.r))
        return self.r[0]