import heapq
from collections import Counter

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        heap = []
        ctr = Counter()
        res = 0
        for i in range(n):
            heapq.heappush(heap, (-values[i], labels[i]))
        while numWanted and len(heap) > 0:
            curr, l = heapq.heappop(heap)
            while ctr[l] == useLimit and len(heap) > 0:
                curr, l = heapq.heappop(heap)
            if ctr[l] < useLimit:
                ctr[l] += 1
                res -= curr
            numWanted -= 1
        return res