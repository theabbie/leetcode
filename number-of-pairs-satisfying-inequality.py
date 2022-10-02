import bisect

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        d = []
        for i in range(n):
            d.append(nums1[i] - nums2[i])
        res = 0
        order = []
        for i in range(n - 1, -1, -1):
            res += len(order) - bisect.bisect_left(order, d[i] - diff)
            bisect.insort(order, d[i])
        return res