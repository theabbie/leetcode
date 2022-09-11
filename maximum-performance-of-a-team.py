import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        n = len(speed)
        vals = []
        for i in range(n):
            vals.append((efficiency[i], speed[i]))
        vals.sort()
        heap = []
        total = 0
        res = 0
        for i in range(n - 1, -1, -1):
            heapq.heappush(heap, vals[i][1])
            total += vals[i][1]
            if len(heap) > k:
                total -= heapq.heappop(heap)
            res = max(res, vals[i][0] * total)
        return res % (10 ** 9 + 7)