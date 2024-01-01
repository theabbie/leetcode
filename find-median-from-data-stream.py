from sortedcontainers import SortedList

class MedianFinder:
    def __init__(self):
        self.l = SortedList()
        self.r = SortedList()

    def addNum(self, num: int) -> None:
        if len(self.r) > 0 and num >= self.r[0]:
            self.r.add(num)
        else:
            self.l.add(num)
        while len(self.l) < len(self.r):
            self.l.add(self.r.pop(0))
        while len(self.l) - len(self.r) > 1:
            self.r.add(self.l.pop(-1))

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return self.l[-1]
        return (self.l[-1] + self.r[0]) / 2