import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        res = 0
        m = len(values)
        n = len(values[0])
        for i in range(m):
            values[i].reverse()
        pos = [0] * m
        heap = []
        for i in range(m):
            if pos[i] < n:
                heapq.heappush(heap, (values[i][pos[i]], i))
                pos[i] += 1
        d = 1
        while len(heap) > 0:
            currval, i = heapq.heappop(heap)
            res += d * currval
            if pos[i] < n:
                heapq.heappush(heap, (values[i][pos[i]], i))
                pos[i] += 1
            d += 1
        return res