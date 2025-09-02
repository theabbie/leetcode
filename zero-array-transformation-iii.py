import heapq

class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort()
        dec = FenwickTree([0] * n)
        i = 0
        heap = []
        res = len(queries)
        for j in range(n):
            while i < len(queries) and queries[i][0] <= j:
                heapq.heappush(heap, (-queries[i][1], queries[i][0]))
                i += 1
            while nums[j] - dec.query(j + 1) > 0 and heap:
                res -= 1
                x = heapq.heappop(heap)
                l, r = x[1], -x[0]
                dec.update(l, 1)
                dec.update(r + 1, -1)
            if nums[j] - dec.query(j + 1) > 0:
                return -1
        return res