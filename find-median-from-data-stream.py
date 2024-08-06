import heapq

class MedianFinder:
    def __init__(self):
        self.l = []
        self.r = []
        
    def balance(self):
        while len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))
        while len(self.l) - len(self.r) > 1:
            heapq.heappush(self.r, -heapq.heappop(self.l))

    def addNum(self, num: int) -> None:
        if self.l and num > -self.l[0]:
            heapq.heappush(self.r, num)
        else:
            heapq.heappush(self.l, -num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return -self.l[0]
        if len(self.l) + len(self.r) == 1:
            return -self.l[0]
        return (-self.l[0] + self.r[0]) / 2