import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        vals = [(nums2[i], nums1[i]) for i in range(n)]
        if k == 1:
            return max(a * b for a, b in vals)
        vals.sort(reverse = True)
        res = 0
        s = 0
        heap = []
        for i in range(n):
            heapq.heappush(heap, vals[i][1])
            s += vals[i][1]
            if len(heap) > k - 1:
                s -= heapq.heappop(heap)
            if len(heap) == k - 1 and i < n - 1:
                res = max(res, vals[i + 1][0] * (vals[i + 1][1] + s))
        return res