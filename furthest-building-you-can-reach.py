import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        total = 0
        totalheap = 0
        for i in range(n - 1):
            if heights[i] < heights[i + 1]:
                diff = heights[i + 1] - heights[i]
                total += diff
                heapq.heappush(heap, diff)
                totalheap += diff
                if len(heap) > ladders:
                    totalheap -= heapq.heappop(heap)
                if total - totalheap > bricks:
                    return i
        return n - 1