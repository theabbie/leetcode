import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        res = float('inf')
        vals = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        vals.sort()
        heap = []
        qsum = 0
        res = float('inf')
        for i in range(n):
            if i >= k - 1:
                res = min(res, vals[i][0] * (vals[i][1] + qsum))
            heapq.heappush(heap, -vals[i][1])
            qsum += vals[i][1]
            while len(heap) > k - 1:
                qsum += heapq.heappop(heap)
        return res