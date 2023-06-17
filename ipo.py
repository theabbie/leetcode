import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pairs = [(capital[i], profits[i]) for i in range(n)]
        pairs.sort()
        i = 0
        curr = w
        heap = []
        while k > 0:
            while i < n and pairs[i][0] <= curr:
                heapq.heappush(heap, -pairs[i][1])
                i += 1
            if len(heap) > 0:
                curr -= heapq.heappop(heap)
                k -= 1
            else:
                break
        return curr