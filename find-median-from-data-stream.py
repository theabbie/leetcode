import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        left = self.left
        right = self.right
        if len(right) == 0:
            heapq.heappush(right, num)
        elif num < right[0]:
            heapq.heappush(left, -num)
        elif num >= right[0]:
            heapq.heappush(right, num)
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        if len(right) > len(left) + 1:
            heapq.heappush(left, -heapq.heappop(right))

    def findMedian(self) -> float:
        left = self.left
        right = self.right
        if len(left) == len(right):
            return (right[0] - left[0]) / 2
        if len(left) > len(right):
            return -left[0]
        if len(left) < len(right):
            return right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()