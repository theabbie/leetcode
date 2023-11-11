import bisect
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [row[::-1] for row in mat]
        heap = []
        for i, row in enumerate(mat):
            strength = -bisect.bisect_left(row, 1)
            heapq.heappush(heap, (strength, i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res