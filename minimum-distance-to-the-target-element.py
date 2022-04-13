import heapq

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (abs(num - target), abs(i - start)))
        return heap[0][1]